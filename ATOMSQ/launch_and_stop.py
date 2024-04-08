# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOMSQ/launch_and_stop.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1978 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import depends, listens
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.components import ClipSlotComponent
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.live import liveobj_valid

class LaunchAndStopComponent(Component):
    scene_launch_button = ButtonControl(color="DefaultButton.Off",
      pressed_color="DefaultButton.On")
    track_stop_button = ButtonControl()

    @depends(target_track=None)
    def __init__(self, target_track=None, *a, **k):
        (super().__init__)(*a, **k)
        self._target_track = target_track
        self._clip_slot = ClipSlotComponent()
        self.register_slot(self._target_track, self._LaunchAndStopComponent__on_track_or_scene_changed, "target_track")
        self.register_slot(self.song.view, self._LaunchAndStopComponent__on_track_or_scene_changed, "selected_scene")
        self._LaunchAndStopComponent__on_playing_status_changed.subject = self._target_track
        self._LaunchAndStopComponent__on_track_or_scene_changed()
        self._LaunchAndStopComponent__on_playing_status_changed()

    def set_clip_launch_button(self, button):
        self._clip_slot.set_launch_button(button)

    @scene_launch_button.pressed
    def scene_launch_button(self, _):
        self.song.view.selected_scene.fire()

    @track_stop_button.pressed
    def track_stop_button(self, _):
        self.song.view.selected_track.stop_all_clips()

    def __on_track_or_scene_changed(self):
        slot = self.song.view.highlighted_clip_slot
        self._clip_slot.set_clip_slot(slot if liveobj_valid(slot) else None)

    @listens("target_track.playing_slot_index")
    def __on_playing_status_changed(self):
        track = self._target_track.target_track
        self.track_stop_button.enabled = track in self.song.tracks and track.playing_slot_index >= 0
