# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/VCM600/MixerComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1570 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import map, range
from _Framework.MixerComponent import MixerComponent as MixerComponentBase
from .TrackEQComponent import TrackEQComponent
from .TrackFilterComponent import TrackFilterComponent

class MixerComponent(MixerComponentBase):

    def __init__(self, num_tracks, *a, **k):
        self._track_eqs = [TrackEQComponent() for _ in range(num_tracks)]
        self._track_filters = [TrackFilterComponent() for _ in range(num_tracks)]
        (super(MixerComponent, self).__init__)(num_tracks, *a, **k)
        list(map(self.register_components, self._track_eqs))
        list(map(self.register_components, self._track_filters))

    def track_eq(self, index):
        return self._track_eqs[index]

    def track_filter(self, index):
        return self._track_filters[index]

    def _reassign_tracks(self):
        super(MixerComponent, self)._reassign_tracks()
        tracks = self.tracks_to_use()
        for index in range(len(self._channel_strips)):
            track_index = self._track_offset + index
            track = tracks[track_index] if len(tracks) > track_index else None
            if len(self._track_eqs) > index:
                self._track_eqs[index].set_track(track)
            if len(self._track_filters) > index:
                self._track_filters[index].set_track(track)
