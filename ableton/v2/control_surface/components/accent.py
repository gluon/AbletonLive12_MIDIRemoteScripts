# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/components/accent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1183 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import listenable_property
from ..component import Component
from ..control import ToggleButtonControl
from ..elements import NullFullVelocity

class AccentComponent(Component):
    accent_button = ToggleButtonControl(toggled_color="Accent.On",
      untoggled_color="Accent.Off")

    def __init__(self, *a, **k):
        (super(AccentComponent, self).__init__)(*a, **k)
        self.set_full_velocity(None)

    def set_full_velocity(self, full_velocity):
        self._full_velocity = full_velocity or NullFullVelocity()
        self.accent_button.is_toggled = self.activated

    @listenable_property
    def activated(self):
        return self._full_velocity.enabled

    @accent_button.toggled
    def accent_button(self, is_toggled, button):
        self._full_velocity.enabled = is_toggled
        self.notify_activated()

    @accent_button.released_delayed
    def accent_button(self, button):
        self.accent_button.is_toggled = False
        self._full_velocity.enabled = False
        self.notify_activated()
