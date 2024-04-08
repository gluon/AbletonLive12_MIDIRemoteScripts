# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/scene_list.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1729 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from future.moves.itertools import zip_longest
from ableton.v2.base import listens
from ableton.v2.control_surface import Component
from .scene import MPCSceneComponent

class SceneListComponent(Component):

    def __init__(self, session_ring=None, num_scenes=0, *a, **k):
        (super(SceneListComponent, self).__init__)(*a, **k)
        self._session_ring = session_ring
        self._SceneListComponent__on_offsets_changed.subject = session_ring
        self._scenes = [MPCSceneComponent(parent=self, session_ring=session_ring) for _ in range(num_scenes)]
        self._SceneListComponent__on_scene_list_changed.subject = self.song
        self._reassign_scenes()

    def set_scene_launch_buttons(self, buttons):
        for scene, button in zip_longest(self._scenes, buttons or []):
            scene.set_launch_button(button)

    def set_scene_color_controls(self, controls):
        for scene, control in zip_longest(self._scenes, controls or []):
            scene.scene_color_control.set_control_element(control)

    @listens("offset")
    def __on_offsets_changed(self, *a):
        if self.is_enabled():
            self._reassign_scenes()

    @listens("scenes")
    def __on_scene_list_changed(self):
        self._reassign_scenes()

    def _reassign_scenes(self):
        scenes = self.song.scenes
        for index, scene in enumerate(self._scenes):
            scene_index = self._session_ring.scene_offset + index
            scene.set_scene(scenes[scene_index] if len(scenes) > scene_index else None)
