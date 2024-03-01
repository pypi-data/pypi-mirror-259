import copy
import logging
import collections

import numpy as np
from qtpy import QtCore
from qtpy.QtGui import QPen
from qtpy.QtCore import Signal
import pyqtgraph as pg

from gpstime import gpstime, gpsnow

from . import util
from . import const
from .plotMenu import NDScopePlotMenu
from . import template
from . import legend
from . import cursors

logger = logging.getLogger('PLOT')


##################################################


# monkey patch to add a set_color_mode method to the AxisItem class

# Copied from pyqtgraph source version 0.12.3.
def _updateLabel(self):
    """Internal method to update the label according to the text"""
    self.label.setHtml(self.labelString())
    self._adjustSize()
    self.picture = None
    self.update()

pg.AxisItem._updateLabel = _updateLabel


def _set_color_mode(self, mode):
    # Modified from pyqtgraph source version 0.12.3 for AxisItem.setTextPen.
    # https://pyqtgraph.readthedocs.io/en/pyqtgraph-0.12.3/_modules/pyqtgraph/graphicsItems/AxisItem.html#AxisItem.setTextPen
    fg = const.COLOR_MODE[mode]['fg']
    pen = QPen(fg)
    self.picture = None
    self._textPen = pen
    self.labelStyle['color'] = self._textPen.color().name()
    self._updateLabel()

pg.AxisItem.set_color_mode = _set_color_mode


##################################################


class TimeStringAxis(pg.AxisItem):
    def __init__(self, orientation='bottom', **kwargs):
        super().__init__(orientation, **kwargs)
        self.t0 = 0
        self.setTickStringsMode('relative')

    def t_to_relative(self, t):
        return str(util.TDStr(t))

    def t_to_gps(self, t):
        return str(t + self.t0)

    def t_to_utc(self, t):
        gps = gpstime.fromgps(t + self.t0)
        return gps.strftime(const.TICK_DATE_FMT)

    def t_to_local(self, t):
        gps = gpstime.fromgps(t + self.t0)
        local = gps.astimezone()
        return local.strftime(const.TICK_DATE_FMT)

    def setTickStringsMode(self, mode):
        func_map = {
            'relative': self.t_to_relative,
            'absolute GPS': self.t_to_gps,
            'absolute UTC': self.t_to_utc,
            'absolute local': self.t_to_local,
        }
        self.tick_func = func_map[mode]
        # this is needed to clear/update the ticks on change:
        self.picture = None
        self.update()
        self.mode = mode

    ######

    def tickSpacing(self, minVal, maxVal, size):
        span = abs(maxVal - minVal)
        for major, minordiv in const.TICK_SPACINGS:
            if span >= 3*major:
                break
        return [
            (major, 0),
            (major/minordiv, 0),
        ]

    def tickStrings(self, values, scale, spacing):
        return [self.tick_func(t) for t in values]


##################################################


class NDScopeViewBox(pg.ViewBox):

    def __init__(self, data_store, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data_store

    # HACK: we overload this function to pass the mouse event to the
    # context menu popup, instead of the global point position, so
    # that the menu can extract the local scene point.  See
    # NDScopePlotMenu.popup
    def raiseContextMenu(self, ev):
        menu = self.getMenu(ev)
        if menu is not None:
            self.scene().addParentContextMenus(self, menu, ev)
            menu.popup(ev)

    def translateBy(self, t=None, x=None, y=None):
        if self.data.online:
            x = None
        super().translateBy(t=t, x=x, y=y)

    def scaleBy(self, s=None, center=None, x=None, y=None):
        if self.data.online:
            if center:
                center = pg.Point(0, center.y())
        super().scaleBy(s=s, center=center, x=x, y=y)

##################################################


class NDScopePlot(pg.PlotItem):
    channel_config_request = Signal('PyQt_PyObject')
    new_plot_request = Signal('PyQt_PyObject')
    remove_plot_request = Signal('PyQt_PyObject')
    t0_reset = Signal(float)
    t_cursors_enable = Signal(bool)
    t_cursor_moved = Signal('PyQt_PyObject')
    log_mode_toggled = Signal('PyQt_PyObject')

    def __init__(self, data_store, *args, title=None, loc=None):
        """Initialize NDSCope Plot object

        """
        super().__init__(
            *args,
            viewBox=NDScopeViewBox(data_store),
            axisItems={'bottom': TimeStringAxis()},
        )

        self.data = data_store
        self.title = title
        self.loc = loc

        # dict of channel:curve
        self.channels = collections.OrderedDict()

        self.t_cursors = cursors.TCursors(self)
        self.t_cursors.cursor_moved.connect(self._update_t_cursor)
        self.y_cursors = cursors.YCursors(self)

        # setup the custom context menu.  should be setup after
        # cursors are created above.  unclear why it needs to be
        # implemented as a ViewBox menu instead of as the "ctrlMenu"
        # for the plot.
        self.ctrlMenu = None
        self.getViewBox().menu = NDScopePlotMenu(self)

        # plot options
        # use automatic downsampling and clipping to reduce the
        # drawing load
        self.setDownsampling(mode='peak')
        # clip data to only what's visible
        # FIXME: is this what we want?
        self.setClipToView(True)
        # don't auto-range x axis, since we have special handling
        self.disableAutoRange(axis='x')
        # hide auto-scale buttons
        self.hideButtons()
        # add legend
        self.legend = legend.Legend()
        self.legend.setParentItem(self.getViewBox())
        self.legend.setVisible(False)
        # show grid lines
        self.showGrid(x=True, y=True, alpha=0.2)
        self.setLabel('left', 'counts')
        # limit the zooming range
        self.setLimits(
            minXRange=0.0001,
        )
        # accept drops
        self.setAcceptDrops(True)

        # If this option is not removed then a default font size will
        # be set in the generated html that will not overridable by
        # setting the font.
        self.titleLabel.opts.pop('size')

    def dropEvent(self, event):
        data = event.mimeData()
        if data.hasFormat('text/plain'):
            text_list = data.text().splitlines()
            for text in text_list:
                self.add_channels({text: None})

    def open_channel_config_dialog(self):
        self.channel_config_request.emit(self)

    def _add_channel_obj(self, cc):
        channel = cc.channel
        self.channels[channel] = cc
        self.addItem(cc.curves['y'])
        self.addItem(cc.curves['bad'])
        self.enableAutoRange(axis='y')
        self._update_title_legend()
        cc.label_changed.connect(self._update_legend_item)
        cc.label_changed.connect(self._update_title_legend)
        cc.unit_changed.connect(self._update_units)
        self._update_legend_item(channel)

    def _remove_channel_obj(self, cc):
        channel = cc.channel
        self.legend.removeItem(cc.get_label())
        for curve in cc.curves.values():
            self.removeItem(curve)
        del self.channels[channel]
        self._update_title_legend()

    def set_channel_objs(self, chan_obj_list):
        """set plot channels from list NDScopePlotChannel objects

        Any channels currently being plotted that are not in list will
        be removed.

        """
        channel_dict = {cc.channel: cc for cc in chan_obj_list}
        set_chans = set(channel_dict.keys())
        cur_chans = set(self.channels.keys())
        with self.data as ds:
            for chan in cur_chans - set_chans:
                ds.remove_channel(chan)
                cc = self.channels[chan]
                self._remove_channel_obj(cc)
            for chan in set_chans - cur_chans:
                ds.add_channel(chan)
                self._add_channel_obj(channel_dict[chan])
            for chan in set_chans & cur_chans:
                self.channels[chan].set_params(**channel_dict[chan].params)
        self.set_y_range('auto')

    def add_channels(self, channel_dict):
        """Add channels to plot

        Takes a dictionary where the keys are channel names and the
        values are channel curve keyword argument dictionaries.  The
        keyword arguments are passed directly to NDScopePlotChannel.

        """
        with self.data as ds:
            for channel, kwargs in channel_dict.items():
                if channel in self.channels:
                    continue
                kwargs = kwargs or {}
                cc = NDScopePlotChannel(channel, **kwargs)
                ds.add_channel(channel)
                self._add_channel_obj(cc)
        self.set_y_range('auto')

    def remove_channels(self, channel_list=None):
        """remove channels from plot

        Takes a list of channel names to remove.  If the
        `channel_list` argument is missing all channels will be
        removed.

        """
        if channel_list is None:
            channel_list = list(self.channels.keys())
        with self.data as ds:
            for channel in channel_list:
                if channel not in self.channels:
                    continue
                ds.remove_channel(channel)
                cc = self.channels[channel]
                self._remove_channel_obj(cc)
        self.set_y_range('auto')

    def get_channels(self):
        """get a channel:params dict for all channels in plot

        """
        return {chan:cc.params for chan, cc in self.channels.items()}

    def set_font(self, font):
        """Set label and axis font"""
        self.titleLabel.item.setFont(font)
        self.legend.setFont(font)
        self.axes['left']['item'].label.setFont(font)
        self.axes['bottom']['item'].setTickFont(font)
        self.axes['left']['item'].setTickFont(font)
        self.t_cursors.set_font(font)
        self.y_cursors.set_font(font)

    def set_color_mode(self, mode):
        fg = const.COLOR_MODE[mode]['fg']
        bg = const.COLOR_MODE[mode]['bg']
        self.titleLabel.setAttr('color', fg)
        self.titleLabel.setText(self.titleLabel.text)
        self.legend.setTextColor(fg)
        self.axes['left']['item'].set_color_mode(mode)
        self.axes['bottom']['item'].set_color_mode(mode)
        self.t_cursors.set_color_mode(mode)
        self.y_cursors.set_color_mode(mode)

    ##### y axis

    @property
    def log_mode(self):
        """current log mode state"""
        return self.getAxis('left').logMode

    def y_pos_to_val(self, y):
        """get the y coordinate position for a given value

        Takes into account logarithmic axis scaling.

        """
        if self.log_mode:
            y = 10 ** y
        return y

    def y_val_to_pos(self, y):
        """get the y value for a given coordinate position

        Takes into account logarithmic axis scaling.  If the value
        doesn't correspond to any position on the axis, None will be
        returned.

        """
        if self.log_mode:
            if y > 0:
                # HACK: we convert to normal float because pyyaml
                # can't handle numpy objects
                return float(np.log10(y))
            else:
                return None
        else:
            return y

    def set_y_range(self, y_range):
        """set the Y axis range

        If None or "auto" then auto range will be enabled, otherwise
        range should be tuple.

        """
        logger.debug(f"plot {self.loc} Y range: {y_range}")
        if y_range in [None, 'auto']:
            self.enableAutoRange(axis='y')
        else:
            self.disableAutoRange(axis='y')
            y_range = tuple(map(self.y_val_to_pos, y_range))
            self.getViewBox().setYRange(*y_range, padding=0.0)

    def set_log_mode(self, log=True):
        """set the Y scale to be log

        True turns on log mode, False turns it off.

        """
        assert isinstance(log, bool)
        # FIXME HACK: This is a hack around
        # https://github.com/pyqtgraph/pyqtgraph/issues/2307 Since we
        # can not stop it from autoscaling the range at least once
        # when we switch on log mode, we keep track of the axis state
        # and set it back after the change.
        vb = self.getViewBox()
        x_range, y_range = vb.viewRange()
        self.setLogMode(y=log)
        vb.disableAutoRange(vb.XAxis)
        vb.setXRange(min=x_range[0], max=x_range[1], padding=0.0)
        self.y_cursors.redraw()
        self.log_mode_toggled.emit(self)

    ##########

    def _reset_t0(self, val):
        self.t0_reset.emit(val)

    ##### cursors

    def enable_t_cursors(self):
        """enable T cursors and return cursor object"""
        if self.t_cursors.C1 not in self.getViewBox().allChildren():
            self.addItem(self.t_cursors.C1, ignoreBounds=True)
            self.addItem(self.t_cursors.C2, ignoreBounds=True)
            self.addItem(self.t_cursors.diff, ignoreBounds=True)
            self.t_cursors.reset()
            logger.debug(f"plot {self.loc} T cursor enabled")
        return self.t_cursors

    def _update_t_cursor(self, indval):
        self.t_cursor_moved.emit(indval)

    def enable_y_cursors(self):
        """enable Y cursors and return cursor object"""
        if self.y_cursors.C1 not in self.getViewBox().allChildren():
            self.addItem(self.y_cursors.C1, ignoreBounds=True)
            self.addItem(self.y_cursors.C2, ignoreBounds=True)
            self.addItem(self.y_cursors.diff, ignoreBounds=True)
            self.y_cursors.reset()
            logger.debug(f"plot {self.loc} Y cursor enabled")
        return self.y_cursors

    ##########

    # SLOT
    def _update_legend_item(self, channel):
        cc = self.channels[channel]
        self.legend.removeItem(cc.curves['y'])
        self.legend.addItem(cc.curves['y'], cc.get_label())

    def _update_title_legend(self):
        """update plot title and legend"""
        if self.title:
            self.legend.setVisible(True)
            self.setTitle(self.title)
        elif len(self.channels) < 1:
            self.legend.setVisible(False)
            self.setTitle(None)
        elif len(self.channels) == 1:
            self.legend.setVisible(False)
            self.setTitle(list(self.channels.values())[0].get_label())
        else:
            self.legend.setVisible(True)
            self.setTitle(None)

    def _update_units(self):
        units = set(
            [cc.get_unit() for cc in self.channels.values()]
        )
        self.setLabel('left', '/'.join(list(units)))

    def clear_data(self):
        """clear data for all channels

        """
        for curve in self.channels.values():
            curve.clear_data()

    def _set_t_limits(self, t0):
        """Set the t axis limits for a given t0"""
        self.setLimits(
            xMin=const.GPS_MIN-t0,
            #xMax=gpsnow()-t0+1,
        )

    def set_all_mean_curves_visibility(self, visible):
        for cc in self.channels.values():
            cc.set_mean_curve_visibility(visible)

    def set_all_min_curves_visibility(self, visible):
        for cc in self.channels.values():
            cc.set_min_curve_visibility(visible)

    def set_all_max_curves_visibility(self, visible):
        for cc in self.channels.values():
            cc.set_max_curve_visibility(visible)

    def update(self, data, t0):
        """update all channel

        `data` should be a DataBufferDict object, and `t0` is the GPS
        time for t=0.

        """
        self.axes['bottom']['item'].t0 = t0
        self._set_t_limits(t0)

        for channel, cc in self.channels.items():
            if channel not in data or not data[channel]:
                continue

            cd = data[channel]

            if cd.is_trend and not cc.is_trend:
                self.addItem(cc.curves['min'])
                self.addItem(cc.curves['max'])
                if cc.curves['fill']:
                    self.addItem(cc.curves['fill'])
            elif not cd.is_trend and cc.is_trend:
                self.removeItem(cc.curves['min'])
                self.removeItem(cc.curves['max'])
                if cc.curves['fill']:
                    self.removeItem(cc.curves['fill'])

            cc.set_data(cd, t0)


##################################################


class NDScopePlotChannel(QtCore.QObject):
    label_changed = Signal(str)
    unit_changed = Signal(str)

    def __init__(self, channel, **kwargs):
        """Initialize channel curve object

        Holds curves for y value, and for trend min/max/fill.

        Keyword arguments are trace style parameters, e.g. `color`,
        `width`, `unit`, `scale` and `offset`.  `color` can be a
        single letter color spec ('b', 'r', etc.), an integer, or an
        [r,g,b] list.  See the following for more info:

          http://www.pyqtgraph.org/documentation/functions.html#pyqtgraph.mkColor

        """
        super().__init__()

        self.channel = channel
        self.params = dict(template.CURVE)
        self.data = None

        self.curves = {}
        self.curves['y'] = pg.PlotDataItem([0, 0], name='')
        self.curves['min'] = pg.PlotDataItem([0, 0])
        self.curves['max'] = pg.PlotDataItem([0, 0])
        # FIXME: fill is expensive, so we disable it until figure it out
        if False:
            self.curves['fill'] = pg.FillBetweenItem(
                self.curves['min'],
                self.curves['max'],
            )
        else:
            self.curves['fill'] = None
        # special curve for bad data (nans, infs)
        self.curves['bad'] = pg.PlotDataItem([0, 0])

        kwargs['color'] = template.get_channel_color(channel, kwargs.get('color'))
        self.set_params(**kwargs)

    def as_tuple(self):
        return (('channel', self.channel),) + tuple(sorted(self.params.items()))

    @property
    def is_trend(self):
        if self.data:
            return self.data.is_trend
        return False

    def __repr__(self):
        return "<{} {} {}>".format(
            self.__class__.__name__,
            self.channel,
            self.params,
        )

    # NOTE: we override the hash and eq definitions for these objects
    # so that we can compare them in sets.  hopefully this doesn't
    # cause any other problems
    def __hash__(self):
        return hash(self.as_tuple())

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def _update_transform(self):
        """update the transform function"""
        if self.params['scale'] != 1 or self.params['offset'] != 0:
            def transform(data):
                return (data + self.params['offset']) * self.params['scale']
        else:
            def transform(data):
                return data
        self.transform = transform

    def _update_label(self):
        self.label_changed.emit(self.channel)

    def _update_unit(self):
        self.unit_changed.emit(self.channel)

    def get_QColor(self):
        """Get channel color as a QColor object"""
        return pg.mkColor(self.params['color'])

    def set_params(self, **params):
        """set parameters for this channel

        """
        PARAMS = ['color', 'width', 'scale', 'offset', 'unit', 'label']

        for param, value in params.items():
            if param not in PARAMS:
                raise KeyError(f"invalid parameter '{param}', options are: {PARAMS}")
            if param == 'color':
                value = pg.mkColor(value).name()
            self.params[param] = value

        color = self.get_QColor()
        pen = pg.mkPen(color, width=self.params['width'])
        mmc = copy.copy(color)
        mmc.setAlpha(const.TREND_MINMAX_ALPHA)
        mmpen = pg.mkPen(mmc, width=self.params['width'], style=QtCore.Qt.DashLine)
        self.curves['y'].setPen(pen)
        self.curves['min'].setPen(mmpen)
        self.curves['max'].setPen(mmpen)
        self.curves['bad'].setPen(
            pg.mkPen('r', width=self.params['width'], style=QtCore.Qt.DotLine)
        )
        if self.curves['fill']:
            self.curves['fill'].setBrush(mmc)
        self._update_label()
        self._update_unit()
        if not set(['scale', 'offset']).isdisjoint(self.params):
            self._update_transform()
            self._redraw_curves()

    def get_unit(self):
        """return channel unit"""
        unit = self.params.get('unit')
        if not unit:
            if self.data:
                unit = self.data.unit or 'counts'
            else:
                unit = 'counts'
        return unit

    def get_label(self):
        if self.params.get('label'):
            return self.params['label']
        offset = self.params['offset']
        scale = self.params['scale']
        label = f'{self.channel}'
        if offset != 0:
            if scale != 1:
                label = f'({self.channel} {offset:+g})'
            else:
                label += f' {offset:+g}'
        if scale != 1:
            label += f'*{scale:g}'
        if self.data and self.data.is_trend:
            label += f' [{self.data.ctype}]'
        return label

    def set_mean_curve_visibility(self, visible):
        self.curves['y'].setVisible(visible)

    def set_min_curve_visibility(self, visible):
        self.curves['min'].setVisible(visible)

    def set_max_curve_visibility(self, visible):
        self.curves['max'].setVisible(visible)

    def clear_data(self):
        """clear data for curves

        """
        self.data = None
        for curve in self.curves.values():
            try:
                curve.setData(np.array([0, 0]))
            except:
                pass

    def _update_curve_data(self, mod, cid, t=None):
        y = self.data[mod]
        if t is None:
            t = self.data.tarray - self.t0
        # FIXME: HACK: replace all +-infs with nans.  the infs
        # were causing the following exception in PlotCurveItem
        # when it tried to find the min/max of the array:
        # ValueError: zero-size array to reduction operation minimum which has no identity
        # using nan is not great, since that's also an indicator
        # of a gap, but not sure what else to use.
        try:
            np.place(y, np.isinf(y), np.nan)
        except ValueError:
            # this check throws a value error if y is int.  but in
            # that case there's nothing we need to convert, so
            # just pass
            pass
        y = self.transform(y)
        self.curves[cid].setData(
            x=t,
            y=y,
            connect="finite",
        )
        return t, y

    def _redraw_curves(self):
        """redraw all data"""
        if not self.data:
            return
        if 'raw' in self.data:
            t, y = self._update_curve_data('raw', 'y')
        else:
            t, y = self._update_curve_data('mean', 'y')
            for mod in ['min', 'max']:
                self._update_curve_data(mod, mod, t)
        return t, y

    def set_data(self, data, t0):
        """set data for curves

        Data should be DataBuffer object.

        """
        if self.data:
            ctype_changed = data.ctype != self.data.ctype
        else:
            ctype_changed = True
        self.data = data
        self.t0 = t0

        t, y = self._redraw_curves()

        self.curves['bad'].setData(
            x=t,
            y=hold_over_nan(y),
            connect="finite",
        )

        if ctype_changed:
            self._update_label()


##################################################


def hold_over_nan(y):
    """hold data over subsequent nans

    This function finds all nans in the input array, and produces an
    output array that is nan everywhere except where the input array
    was nan.  Where the input array was nan, the output array will be
    the value of the input array right before the nan.  If the first
    element of the input array is nan then zero will be used.
    Example:

    y   = [nan, nan,   2,   3,   4,   5, nan, nan, nan,   9,  10]
    out = [  0,   0,   0, nan, nan,   5,   5,   5,   5,   5, nan]

    We use this for indicating "bad" data regions in plots.

    """
    nani = np.where(np.isnan(y))[0]
    if nani.size == y.size:
        return np.zeros_like(y, dtype=float)
    out = np.empty_like(y, dtype=float)
    out[:] = np.nan
    if nani.size == 0:
        return out
    ti = np.where(np.diff(nani) > 1)[0]
    nstart = np.append(nani[0], nani[ti+1])
    nend = np.append(nani[ti], nani[-1]) + 1
    for s, e in zip(nstart, nend):
        if s == 0:
            v = 0
        else:
            v = y[s-1]
        out[s-1:e+1] = v
    return out
