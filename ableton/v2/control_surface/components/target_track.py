# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/components/target_track.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3202 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import filter
from ableton.v2.base import listens, listens_group, liveobj_valid
from ableton.v2.control_surface import Component

class TargetTrackComponent(Component):
    __events__ = ('target_track', )

    def __init__(self, *a, **k):
        (super(TargetTrackComponent, self).__init__)(*a, **k)
        self._target_track = None
        self._armed_track_list = []
        self._TargetTrackComponent__on_selected_track_changed.subject = self.song.view
        self._TargetTrackComponent__on_selected_track_changed()

    @property
    def target_track(self):
        return self._target_track

    @listens("selected_track")
    def __on_selected_track_changed(self):
        if not self._armed_track_list:
            self._set_target_track()

    def _set_target_track(self):
        new_target = self._target_track
        if self._armed_track_list:
            new_target = self._armed_track_list[-1]
        else:
            new_target = self.song.view.selected_track
        if self._target_track != new_target:
            self._target_track = new_target
            self.notify_target_track()


class ArmedTargetTrackComponent(TargetTrackComponent):

    def __init__(self, *a, **k):
        (super(ArmedTargetTrackComponent, self).__init__)(*a, **k)
        self._ArmedTargetTrackComponent__on_tracks_changed.subject = self.song
        self._ArmedTargetTrackComponent__on_tracks_changed()

    @property
    def tracks(self):
        return list(filter((lambda t: liveobj_valid(t) and t.can_be_armed and t.has_midi_input), self.song.tracks))

    @listens("visible_tracks")
    def __on_tracks_changed(self):
        tracks = self.tracks
        self._ArmedTargetTrackComponent__on_arm_changed.replace_subjects(tracks)
        self._ArmedTargetTrackComponent__on_frozen_state_changed.replace_subjects(tracks)
        self._refresh_armed_track_list()

    @listens_group("arm")
    def __on_arm_changed(self, _):
        self._refresh_armed_track_list()

    @listens_group("is_frozen")
    def __on_frozen_state_changed(self, _):
        self._refresh_armed_track_list()

    def _refresh_armed_track_listParse error at or near `POP_BLOCK' instruction at offset 60