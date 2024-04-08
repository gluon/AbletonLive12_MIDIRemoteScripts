# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/session_navigation.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 740 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from ableton.v2.control_surface.control import EncoderControl

class SessionNavigationComponent(SessionNavigationComponentBase):
    scene_encoder = EncoderControl()

    @scene_encoder.value
    def scene_encoder(self, value, _):
        if value > 0:
            if self._vertical_banking.can_scroll_up():
                self._vertical_banking.scroll_up()
        elif self._vertical_banking.can_scroll_down():
            self._vertical_banking.scroll_down()
