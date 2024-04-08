# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/clip_launch_component.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1063 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.component import Component
from ableton.v2.control_surface.control import ButtonControl

class ClipLaunchComponent(Component):
    clip_launch_button = ButtonControl()
    track_stop_button = ButtonControl()

    @clip_launch_button.pressed
    def clip_launch_button(self, _):
        song_view = self.song.view
        slot_or_scene = song_view.selected_scene if self.song.view.selected_track == self.song.master_track else song_view.highlighted_clip_slot
        if liveobj_valid(slot_or_scene):
            slot_or_scene.fire()

    @track_stop_button.pressed
    def track_stop_button(self, _):
        track = self.song.view.selected_track
        if track == self.song.master_track:
            self.song.stop_all_clips()
        else:
            if track in self.song.tracks:
                track.stop_all_clips()
