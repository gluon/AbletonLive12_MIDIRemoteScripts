# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/mode.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 655 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.mode import ImmediateBehaviour

class ReenterBehaviour(ImmediateBehaviour):

    def __init__(self, on_reenter=None, *a, **k):
        (super(ReenterBehaviour, self).__init__)(*a, **k)
        self.on_reenter = on_reenter

    def press_immediate(self, component, mode):
        was_active = component.selected_mode == mode
        super(ReenterBehaviour, self).press_immediate(component, mode)
        if was_active:
            self.on_reenter()
