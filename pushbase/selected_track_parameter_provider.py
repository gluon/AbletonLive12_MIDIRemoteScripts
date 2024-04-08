# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/selected_track_parameter_provider.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2683 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import zip
from ableton.v2.base import depends, listens, liveobj_valid
from ableton.v2.control_surface import ParameterProvider
from .mixer_utils import is_set_to_split_stereo
SEND_PARAMETER_NAMES = ('Send A', 'Send B', 'Send C', 'Send D', 'Send E', 'Send F',
                        'Send G', 'Send H', 'Send I', 'Send J', 'Send K', 'Send L')

def toggle_arm(track_to_arm, song, exclusive=False):
    if track_to_arm.can_be_armed:
        track_to_arm.arm = not track_to_arm.arm
        if exclusive:
            if track_to_arm.implicit_arm or track_to_arm.arm:
                for track in song.tracks:
                    if track.can_be_armed and track != track_to_arm:
                        track.arm = False


class SelectedTrackParameterProvider(ParameterProvider):

    @depends(song=None)
    def __init__(self, song=None, *a, **k):
        (super(SelectedTrackParameterProvider, self).__init__)(*a, **k)
        self._track = None
        self._on_selected_track.subject = song.view
        self._on_visible_tracks.subject = song
        self._on_selected_track()

    @property
    def parameters(self):
        if self._track:
            mixer = self._track.mixer_device
            params = [mixer.volume]
            if is_set_to_split_stereo(mixer):
                params += [mixer.left_split_stereo, mixer.right_split_stereo]
            else:
                params += [mixer.panning]
            params += list(mixer.sends)
            return [self._create_parameter_info(p, n) for n, p in zip(self._track_parameter_names(), params)]
        return []

    def _track_parameter_names(self):
        names = ('Volume', )
        names += ('L Split', 'R Split') if is_set_to_split_stereo(self._track.mixer_device) else ('Pan', )
        return names + SEND_PARAMETER_NAMES

    def _create_parameter_info(self, parameter, name):
        raise NotImplementedError()

    @listens("visible_tracks")
    def _on_visible_tracks(self):
        self.notify_parameters()

    @listens("selected_track")
    def _on_selected_track(self):
        self._track = self._on_selected_track.subject.selected_track
        self._on_panning_mode_changed.subject = self._track.mixer_device if liveobj_valid(self._track) else None
        self.notify_parameters()

    @listens("panning_mode")
    def _on_panning_mode_changed(self):
        self.notify_parameters()