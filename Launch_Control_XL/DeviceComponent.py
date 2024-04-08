# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control_XL/DeviceComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2780 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Control import ButtonControl, control_list
from _Framework.DeviceComponent import DeviceComponent as DeviceComponentBase
from _Framework.ModesComponent import EnablingModesComponent, tomode

class DeviceComponent(DeviceComponentBase):
    parameter_lights = control_list(ButtonControl,
      control_count=8,
      enabled=False,
      color="Device.Parameters",
      disabled_color="Device.NoDevice")
    prev_device_button = ButtonControl(color="DefaultButton.On")
    next_device_button = ButtonControl(color="DefaultButton.On")

    @prev_device_button.pressed
    def prev_device_button(self, button):
        self._scroll_device_view(Live.Application.Application.View.NavDirection.left)

    @next_device_button.pressed
    def next_device_button(self, button):
        self._scroll_device_view(Live.Application.Application.View.NavDirection.right)

    def _scroll_device_view(self, direction):
        self.application().view.show_view("Detail")
        self.application().view.show_view("Detail/DeviceChain")
        self.application().view.scroll_view(direction, "Detail/DeviceChain", False)

    def set_device(self, device):
        super(DeviceComponent, self).set_device(device)
        for light in self.parameter_lights:
            light.enabled = bool(device)

    def set_bank_buttons(self, buttons):
        for button in buttons or []:
            if button:
                button.set_on_off_values("Device.BankSelected", "Device.BankUnselected")

        super(DeviceComponent, self).set_bank_buttons(buttons)

    def _is_banking_enabled(self):
        return True


class DeviceModeComponent(EnablingModesComponent):
    device_mode_button = ButtonControl()

    def __init__(self, device_settings_mode=None, *a, **k):
        (super(DeviceModeComponent, self).__init__)(*a, **k)
        self._device_settings_mode = tomode(device_settings_mode)

    @device_mode_button.released_immediately
    def device_mode_button(self, button):
        self.cycle_mode()

    @device_mode_button.pressed_delayed
    def device_mode_button(self, button):
        self.selected_mode = "enabled"
        self._device_settings_mode.enter_mode()

    @device_mode_button.released_delayed
    def device_mode_button(self, button):
        self._device_settings_mode.leave_mode()

    def _update_buttons(self, selected_mode):
        self.device_mode_button.color = "DefaultButton.On" if selected_mode == "enabled" else "DefaultButton.Off"
        super(DeviceModeComponent, self)._update_buttons(selected_mode)
