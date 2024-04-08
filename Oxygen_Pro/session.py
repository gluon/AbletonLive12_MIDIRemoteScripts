# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/session.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 948 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionComponent as SessionComponentBase
from ableton.v2.control_surface.control import ButtonControl, EncoderControl

class SessionComponent(SessionComponentBase):
    selected_scene_launch_button = ButtonControl()
    scene_encoder = EncoderControl()

    @scene_encoder.value
    def scene_encoder(self, value, _):
        factor = 1 if value < 0 else -1
        new_scene_index = factor + list(self.song.scenes).index(self.song.view.selected_scene)
        if new_scene_index in range(len(self.song.scenes)):
            self.song.view.selected_scene = self.song.scenes[new_scene_index]

    @selected_scene_launch_button.released_immediately
    def selected_scene_launch_button(self, _):
        self.song.view.selected_scene.fire()
