# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/channel_strip.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1656 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens, liveobj_valid
from ableton.v2.control_surface.components import ChannelStripComponent as ChannelStripComponentBase
from ableton.v2.control_surface.control import SendValueControl
from .util import get_midi_color_value_for_track

class ChannelStripComponent(ChannelStripComponentBase):
    empty_color = "Mixer.EmptyTrack"
    track_color_control = SendValueControl()
    static_color_control = SendValueControl()

    def __init__(self, *a, **k):
        (super(ChannelStripComponent, self).__init__)(*a, **k)
        self._static_color_value = 0
        self._track_color_value = 0

    def set_static_color_value(self, value):
        if value is not None:
            self._static_color_value = value
            self._update_static_color_control()

    def set_track(self, track):
        super(ChannelStripComponent, self).set_track(track)
        self._ChannelStripComponent__on_track_color_changed.subject = track if liveobj_valid(track) else None
        self._ChannelStripComponent__on_track_color_changed()
        self._update_static_color_control()

    @listens("color")
    def __on_track_color_changed(self):
        self._track_color_value = get_midi_color_value_for_track(self._track)
        self._track_color_changed()

    def _track_color_changed(self):
        self.track_color_control.value = self._track_color_value

    def _update_static_color_control(self):
        self.static_color_control.value = self._static_color_value if liveobj_valid(self._track) else 0
