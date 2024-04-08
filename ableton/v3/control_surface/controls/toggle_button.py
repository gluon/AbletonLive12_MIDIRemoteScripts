# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/controls/toggle_button.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1317 bytes
from __future__ import absolute_import, print_function, unicode_literals
from . import ButtonControl, Connectable, control_event

class ToggleButtonControl(ButtonControl):
    toggled = control_event("toggled")

    class State(ButtonControl.State, Connectable):
        requires_listenable_connected_property = True

        def connect_property(self, *a):
            (super().connect_property)(*a)
            self.is_on = self.connected_property_value

        def on_connected_property_changed(self, value):
            self.is_on = value

        def _on_pressed(self):
            super()._on_pressed()
            self.is_on = not self._is_on
            self._call_listener("toggled", self.is_on)
            self.connected_property_value = self.is_on
