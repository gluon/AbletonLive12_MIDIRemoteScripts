# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/simple_device.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1922 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.moves.itertools import zip_longest
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.control import ControlList, SendValueControl
from novation.launchpad_elements import SESSION_WIDTH
from novation.simple_device import SimpleDeviceParameterComponent as SimpleDeviceParameterComponentBase
from .control import SendReceiveValueControl
DEVICE_FADER_BANK = 3

class SimpleDeviceParameterComponent(SimpleDeviceParameterComponentBase):
    static_color_controls = ControlList(SendValueControl, 8)
    stop_fader_control = SendReceiveValueControl()

    def __init__(self, static_color_value=0, *a, **k):
        self._static_color_value = static_color_value
        (super(SimpleDeviceParameterComponent, self).__init__)(a, use_parameter_banks=True, **k)
        self._update_static_color_controls()
        self._next_bank_index = self.bank_index

    def _on_bank_select_button_checked(self, button):
        self.stop_fader_control.send_value(DEVICE_FADER_BANK)
        self._next_bank_index = button.index

    @stop_fader_control.value
    def stop_fader_control(self, value, _):
        self.bank_index = self._next_bank_index

    def update(self):
        super(SimpleDeviceParameterComponent, self).update()
        self._update_static_color_controls()

    def _update_static_color_controls(self):
        if liveobj_valid(self._device) and self.selected_bank:
            for control, param in zip_longest(self.static_color_controls, self.selected_bank):
                color = self._static_color_value if liveobj_valid(param) else 0
                control.value = color

        else:
            for control in self.static_color_controls:
                control.value = 0
