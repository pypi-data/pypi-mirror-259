from dateutil.tz import tzutc, tzlocal
from qtpy import QtCore
from qtpy.QtCore import Qt
from qtpy.QtCore import Signal
import pyqtgraph as pg

from . import util
from .const import COLOR_MODE, LABEL_ALPHA


class Crosshair(QtCore.QObject):
    signal_position = Signal('PyQt_PyObject')

    pen = pg.mkPen(style=Qt.DotLine)

    def __init__(self):
        """crosshair needs scope to get t0 value"""
        super().__init__()

        self.hline = pg.InfiniteLine(
            angle=0,
            pen=self.pen,
            movable=False,
        )
        self.vline = pg.InfiniteLine(
            angle=90,
            pen=self.pen,
            movable=False,
        )
        self.label = pg.TextItem(
            anchor=(1, 1),
            fill=(0, 0, 0, LABEL_ALPHA),
        )
        self.active_plot = None
        self.pos = None
        self.t0 = None

    def set_font(self, font):
        """Set text label font"""
        self.label.textItem.setFont(font)

    def set_color_mode(self, mode):
        fg = COLOR_MODE[mode]['fg']
        bg = COLOR_MODE[mode]['bg']
        fill_color = bg.color()
        fill_color.setAlpha(LABEL_ALPHA)
        self.label.fill.setColor(fill_color)
        self.label.setColor(fg)
        self.hline.pen.setColor(fg)
        self.vline.pen.setColor(fg)

    def set_active_plot(self, plot):
        if plot == self.active_plot:
            return
        if self.active_plot:
            self.active_plot.removeItem(self.hline)
            self.active_plot.removeItem(self.vline)
            self.active_plot.removeItem(self.label)
            self.active_plot = None
        if plot:
            plot.addItem(self.hline, ignoreBounds=True)
            plot.addItem(self.vline, ignoreBounds=True)
            plot.addItem(self.label, ignoreBounds=True)
            self.active_plot = plot

    def update(self, plot, pos, t0):
        self.set_active_plot(plot)
        self.pos = pos
        self.t0 = t0
        ppos = plot.vb.mapSceneToView(pos)
        x = ppos.x()
        y = ppos.y()
        (xmin, xmax), (ymin, ymax) = plot.viewRange()
        if x > (xmin+xmax)/2:
            ax = 1
        else:
            ax = 0
        if y < (ymin+ymax)/2:
            ay = 1
        else:
            ay = 0
        self.hline.setPos(y)
        self.vline.setPos(x)
        self.label.setPos(x, y)
        self.label.setAnchor((ax, ay))
        t = t0 + x
        y = plot.y_pos_to_val(y)
        fmt = '%Y/%m/%d %H:%M:%S %Z'
        gt = util.gpstime_parse(t)
        greg_utc = gt.astimezone(tzutc()).strftime(fmt)
        greg_local = gt.astimezone(tzlocal()).strftime(fmt)
        label = '''<table>
<tr><td rowspan="3" valign="middle">T=</td><td>{:0.7f}</td></tr>
<tr><td>{}</td></tr>
<tr><td>{}</td></tr>
<tr><td>Y=</td><td>{:g}</td></tr>
</table></nobr>'''.format(t, greg_utc, greg_local, y)
        self.label.setHtml(label)
        self.signal_position.emit((t, greg_utc, greg_local, y))

    def update_t(self, dt):
        x = self.vline.value()
        y = self.hline.value()
        x += dt
        self.vline.setPos(x)
        self.label.setPos(x, y)

    def redraw(self):
        if self.active_plot and self.pos and self.t0:
            self.update(self.active_plot, self.pos, self.t0)
