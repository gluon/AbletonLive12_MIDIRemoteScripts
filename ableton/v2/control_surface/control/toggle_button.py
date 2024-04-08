# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/control/toggle_button.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2973 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .button import ButtonControlBase
from .control import Connectable, control_color, control_event

class ToggleButtonControl(ButtonControlBase):
    toggled = control_event("toggled")

    class State(ButtonControlBase.State, Connectable):
        untoggled_color = control_color("DefaultButton.Off")
        toggled_color = control_color("DefaultButton.On")
        requires_listenable_connected_property = True

        def __init__(self, untoggled_color=None, toggled_color=None, *a, **k):
            (super(ToggleButtonControl.State, self).__init__)(*a, **k)
            if untoggled_color is not None:
                self.untoggled_color = untoggled_color
            if toggled_color is not None:
                self.toggled_color = toggled_color
            self._is_toggled = False

        @property
        def is_toggled(self):
            return self._is_toggled

        @is_toggled.setter
        def is_toggled(self, toggled):
            if self._is_toggled != toggled:
                self._is_toggled = toggled
                self._send_current_color()

        def connect_property(self, *a):
            (super(ToggleButtonControl.State, self).connect_property)(*a)
            self.is_toggled = self.connected_property_value

        def on_connected_property_changed(self, value):
            self.is_toggled = value

        def _send_button_color(self):
            self._control_element.set_light(self.toggled_color if self._is_toggled else self.untoggled_color)

        def _on_pressed(self):
            super(ToggleButtonControl.State, self)._on_pressed()
            self._is_toggled = not self._is_toggled
            self._call_listener("toggled", self._is_toggled)
            self.connected_property_value = self.is_toggled
