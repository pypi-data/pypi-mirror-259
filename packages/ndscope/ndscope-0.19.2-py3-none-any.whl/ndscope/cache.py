import logging
import traceback
import collections

import numpy as np
from qtpy import QtCore
from qtpy.QtCore import Signal, Slot

from gpstime import gpsnow

from . import nds
from . import const
from .data import DataBufferDict
from .exceptions import UnknownChannelError


logger = logging.getLogger('DATA ')


class DataCache(QtCore.QObject):
    # signals
    #
    # channel list read
    signal_channel_list_ready = Signal()
    # channel add/remove attempt
    # payload: (channel, error or None)
    signal_channel_change = Signal('PyQt_PyObject')
    # network data retrieval has started
    # payload: message string
    signal_data_online_start = Signal(str)
    signal_data_retrieve_start = Signal(str)
    # network data retrieval has completed
    # payload: tuple of
    #   error string
    #   active thread bool
    signal_data_online_done = Signal('PyQt_PyObject')
    signal_data_retrieve_done = Signal('PyQt_PyObject')
    # data buffer in response to data request
    # payload: tuple of
    #   trend type string
    #   trend data buffer
    signal_data = Signal('PyQt_PyObject')

    TREND_TYPES = ['raw', 'sec', 'min']

    def __init__(self):
        super().__init__()
        # use a counter to hold references to the channels, so that as
        # many channel references as needed can be added, while only
        # storing one set of channel data
        self._channels = collections.Counter()
        self.last_trend = None
        self.last_start_end = None
        self.restart_requested = False
        self.threads = {}
        self.reset()
        self.set_lookback(2)
        self.available_channels = None
        # sets up call to fetch channel list once the main loop starts
        QtCore.QTimer.singleShot(0, self.fetch_channel_list_async)
        logger.debug("data store initialized")

    def __getitem__(self, mod):
        return self.db[mod]

    def set_lookback(self, lookback):
        self.lookback = lookback
        for bd in self.db.values():
            if bd:
                bd.set_lookback(lookback)

    ##########

    def _emit_data(self, trend, online=False):
        if trend is None:
            self.signal_data.emit((None, None, online))
        elif self.db[trend]:
            self.signal_data.emit((self.db[trend], trend, online))

    ##########

    def fetch_channel_list_async(self):
        if self.available_channels:
            return
        self.remote_cmd('find_channels')

    @property
    def channels(self):
        """list of all channels in the store"""
        # the "+ Counter()" is a way to exclude elements with less
        # than zero referrents (even though we should never hold a
        # channel with zero referents)
        return list(self._channels + collections.Counter())

    @property
    def empty(self):
        """True if there are no channels in the store"""
        return len(self.channels) == 0

    ##########
    # context manager for adding/removing channels
    #
    # This helps coordinating restarts of online streams in case of
    # channel list changes.  once all channel adds/removes are done,
    # any online streams will be restarted if needed.

    def __enter__(self):
        # FIXME: should probably acquire some kind of lock while we're
        # doing this...

        # cache the set of channels we have before the add/remove
        # operations
        self.orig_chan_set = set(self.channels)

        return self

    def add_channel(self, channel):
        """add a channel to the data store

        should be run in context manager to handle online restarts

        """
        if self.available_channels and channel not in self.available_channels:
            error = f"Unknown channel '{channel}'."
            self.signal_channel_change.emit(error)
            raise UnknownChannelError(error)
        self._channels[channel] += 1
        logger.debug("ref count channel '{}': {}".format(channel, self._channels[channel]))
        assert self._channels[channel] > 0
        # if this is not first reference to channel, return
        if self._channels[channel] > 1:
            return
        logger.info(f"channel added: {channel}")

    def remove_channel(self, channel):
        """remove a channel from the data store

        should be run in context manager to handle online restarts

        """
        self._channels[channel] -= 1
        logger.debug("ref count channel '{}': {}".format(channel, self._channels[channel]))
        assert self._channels[channel] >= 0
        # if we still have references to the channel we're done
        if self._channels[channel] != 0:
            return
        logger.info(f"channel removed: {channel}")
        # if not online, delete references to the channel in the
        # cache.  if we are online the cache will be reset during the
        # subsequent restart
        if not self.online:
            for dbd in self.db.values():
                if channel in dbd:
                    del dbd[channel]

    def __exit__(self, exc_type, exc_val, exc_tb):
        cur_chan_set = set(self.channels)
        # if the new set of channels matches the previous set then
        # we're done
        if cur_chan_set == self.orig_chan_set:
            return
        # if online signal the change and restart any online streams
        if self.online:
            self.online_restart()
        # if not online, backfill trend data in the cache. if we are
        # online the cache will be completely reset, so don't bother
        else:
            new_chans = list(cur_chan_set - self.orig_chan_set)
            for trend in self.TREND_TYPES:
                if not self.db[trend]:
                    continue
                self.remote_cmd(
                    'extend',
                    trend=trend,
                    channels=new_chans,
                    start_end=self.db[trend].range,
                )
        self.signal_channel_change.emit(None)

    ##########

    def reset(self):
        """reset the data store (clear all data)"""
        logger.debug("RESET")
        self.db = {k: {} for k in self.TREND_TYPES}
        self._emit_data(None)

    def online_stop(self):
        """stop online stream"""
        logger.debug("ONLINE STOP")
        thread = self.threads.get('online')
        if thread:
            thread.stop()

    def online_start(self, trend, lookback):
        """start online stream

        """
        logger.debug(f"ONLINE START {trend} {lookback}")
        if self.restart_requested:
            logger.debug("restart already requested")
            return
        # no support for min trends, see below
        if trend == 'min':
            trend = 'sec'
        self.last_trend = trend
        self.set_lookback(lookback)
        self._start_or_restart()

    def online_restart(self):
        """restart online stream

        """
        logger.debug(f"ONLINE RESTART")
        if self.restart_requested:
            logger.debug("restart already requested")
            return
        self._start_or_restart()

    def _start_or_restart(self):
        if self.online:
            self.restart_requested = True
            self.signal_data_online_done.connect(self._start)
            self.online_stop()
        else:
            self._start()

    def _start(self):
        logger.debug("_START")
        try:
            self.signal_data_online_done.disconnect(self._start)
        except TypeError:
            pass
        # FIXME: this reset is needed for the backfill to work
        # cleanly.  could maybe backfill all the channels
        # individually, to save what we already have
        self.reset()
        self.signal_data.connect(self._online_backfill)
        self.remote_cmd('online', trend=self.last_trend, channels=self.channels)
        self.restart_requested = False

    def _online_backfill(self, recv):
        """backfill data on online start"""
        logger.debug("_BACKFILL")
        bufs, trend, online = recv
        if not trend:
            return
        self.signal_data.disconnect(self._online_backfill)
        start, end = self.db[trend].range
        start -= self.lookback
        self.remote_cmd('extendleft', trend=trend, channels=self.channels, start_end=(start, end))

    def _min_stop_request(self):
        self.signal_data_online_done.disconnect(self._min_stop_request)
        self.request(self.last_trend, self.last_start_end)

    def request(self, trend, start_end):
        """Request data

        promptly emits signal_data with all on-hand data for trend,
        then triggers remote requests to fill in what is missing.

        `trend` should be one of ['raw', 'sec', 'min'], and
        `start_end` should be a tuple of (start, end) times.

        """
        logger.debug("REQUEST: {} {}".format(trend, start_end))

        assert trend in self.TREND_TYPES
        self.last_trend = trend
        start, end = start_end
        assert end > start

        # FIXME: we really need to do something to put a check on the
        # length of the request.  It really should be based on the
        # bytes being requested, but we don't know the sample rate a
        # priori.
        span = abs(end - start)
        max_seconds = const.TREND_MAX_SECONDS[trend]
        if span > max_seconds:
            self.signal_data_retrieve_done.emit((
                f"Requested span too large: {max_seconds} seconds max for {trend} trend",
                self.active()
            ))
            return

        now = gpsnow()

        if self.online:
            if trend == 'min':
                # no support for min trends.  the iteration time is
                # too slow, until we have a way to forcibly
                # terminating threads
                self.last_start_end = start_end
                self.signal_data_online_done.connect(self._min_stop_request)
                self.online_stop()
                return
            elif trend != self.online:
                self.online_restart()
                return
            # note we continue if online and trend is not changing
            self.set_lookback(np.ceil(abs(now - start)))

        # expand range to ints
        rstart = int(start)
        rend = int(np.ceil(end))

        if rstart > now:
            # self.signal_data_retrieve_done.emit("Requested start time in the future.")
            return

        # add padding
        pad = int((rend - rstart) * const.DATA_SPAN_PADDING)
        rstart -= pad
        rend += pad

        # FIXME: this is to prevent requesting data from the future.
        # The -10 is because the NDS servers don't cover the first few
        # seconds of online data, which should be fixed in the
        # servers.
        if not self.online:
            rend = min(rend, now - 1)

        if rend <= rstart:
            return

        # if the requested trend is empty, just get full span
        if not self.db[trend]:
            self.remote_cmd('extend', trend=trend, channels=self.channels, start_end=(rstart, rend))
            return

        # get current start/end times, adjusting inward to make sure
        # we account for non-second aligned data due to 16Hz online
        dstart, dend = self.db[trend].range
        dstart = int(np.ceil(dstart))
        dend = int(dend)

        # if the requrest is fully for a discontiguous range then
        # clear the cache and make a request for fresh data
        if rstart >= dend or rend < dstart:
            logger.log(5, "CLEAR: {}".format(trend))
            self.db[trend] = {}
            self.remote_cmd('extend', trend=trend, channels=self.channels, start_end=(rstart, rend))
            return

        # emit what data we have (in case the caller is requesting
        # a trend change), and will emit more below if it turns
        # out we need to extend the range
        #self.signal_data.emit(self.db[trend])
        self._emit_data(trend)

        if rstart < dstart:
            self.remote_cmd('extendleft', trend=trend, channels=self.channels, start_end=(rstart, dstart))

        if dend < rend:
            self.remote_cmd('extend', trend=trend, channels=self.channels, start_end=(dend, rend))

    ##########

    def _command_description(self, cmd, trend):
        if cmd == 'online':
            desc = 'online '
        else:
            desc = ''
        if trend == 'sec':
            desc += "second trend data"
        elif trend == 'min':
            desc += "minute trend data"
        elif trend == 'raw':
            desc += "raw data"
        return desc

    def remote_cmd(self, cmd, **kwargs):
        # the thread ID (tid) is used as a kind of primitive lock.
        # the ID should be unique enough to block requests from
        # similar trend/action combos.
        if cmd == 'find_channels':
            tid = 'find_channels'
            desc = "channel list"
            recv_cmd = self.remote_recv_channels
        elif cmd == 'online':
            if not kwargs.get('channels'):
                return
            trend = kwargs['trend']
            tid = 'online'
            desc = self._command_description(cmd, trend)
            recv_cmd = self.remote_recv_data
        else:
            if not kwargs.get('channels'):
                return
            trend = kwargs['trend']
            tid = f'{cmd}-{trend}'
            desc = self._command_description(cmd, trend)
            recv_cmd = self.remote_recv_data

        logger.debug(f"CMD: {cmd} {kwargs}")
        if self.active(tid):
            logger.debug("BUSY: {}".format(tid))
            return
        if self.online and cmd == 'extend':
            logger.debug("BUSY: no extend while online")
            return

        msg = f"Retrieving {desc}..."
        if cmd == 'online':
            self.signal_data_online_start.emit(msg)
        self.signal_data_retrieve_start.emit(msg)

        t = nds.NDSThread(tid, cmd, **kwargs)
        self.threads[tid] = t
        t.new_data.connect(recv_cmd)
        t.done.connect(self.remote_done)
        t.start()

    @Slot('PyQt_PyObject')
    def remote_recv_channels(self, channels):
        nchannels = len(channels)
        logger.info(f'channel list received: {nchannels} channels')
        self.available_channels = channels
        self.signal_channel_list_ready.emit()

    @Slot('PyQt_PyObject')
    def remote_recv_data(self, recv):
        logger.log(5, "")
        logger.log(5, f"RECV: {recv}")
        cmd, trend, buffers = recv
        # FIXME: should the NDS object just return this directly?
        dbd = DataBufferDict(buffers)
        dbd.set_lookback(self.lookback)
        if not self.db.get(trend):
            self.db[trend] = dbd
        elif cmd == 'online':
            try:
                self.db[trend].append(dbd)
            # FIXME: when channels are removed, it's possible for
            # remant buffers to come in on the previous stream that
            # still have the old channels.  In that case the append
            # will produce a KeyError, and we'll just drop the buffer
            # altogether.  This is a little roundabout, and should
            # probaby be handled in a cleaner way.
            except KeyError:
                return
        elif cmd == 'extendleft':
            try:
                self.db[trend].extendleft(dbd)
            # FIXME: this is a hack to get around the fact that left
            # extension during online (which comes about during zoom
            # out, or during pan/zoom right after stop) will sometimes
            # fail if the left end falls off the lookback while
            # waiting for tid "left" to return.  Maybe this is the
            # best thing to do here, but it seems inelegant.  We have
            # no guarantee when the left extend will return, though,
            # and during online appends keep happening, so maybe even
            # if we can be more clever to avoid unnecessary left
            # extend calls that are likely to fail, we probably still
            # want to catch this error during online mode.
            except AssertionError:
                logger.info(traceback.format_exc(0))
        elif cmd == 'extend':
            self.db[trend].extend(dbd)
        self._emit_data(trend, online=cmd=='online')

    @Slot('PyQt_PyObject')
    def remote_done(self, recv):
        logger.debug(f"DONE: {recv}")
        tid, error = recv
        if error:
            error = f"NDS error ({tid}): {error}"
            logger.warning(error)
        signal = (error, self.active())
        if tid == 'online':
            self.signal_data_online_done.emit(signal)
        self.signal_data_retrieve_done.emit(signal)

    def active(self, tid=None):
        """data retrieval activity status of store

        Returns True or False depending on if the specified thread is
        active, or if any thread is active if none specified.

        """
        if tid:
            thread = self.threads.get(tid)
            if not thread:
                return False
            return not thread.isFinished()
        for thread in self.threads.values():
            if not thread.isFinished():
                return True
        return False

    @property
    def online(self):
        """online status of store

        If online active returns the trend of online retrieval,
        otherwise returns False.

        """
        thread = self.threads.get('online')
        if not thread:
            return False
        if thread.isFinished():
            return False
        return thread.kwargs['trend']

    def stop(self):
        logger.debug("STOP")
        # stop data retrieval threads but not the find_channels
        for name, thread in self.threads.items():
            if name == 'find_channels':
                continue
            thread.stop()
            # FIXME: thread terminate is causing problems on SL7
            # thread.terminate()
