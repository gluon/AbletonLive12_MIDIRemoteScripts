# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/SpecialDeviceComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 947 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.DeviceComponent as DeviceComponent
from .consts import DEVICE_MAP_CHANNEL, FADER_TYPE_STANDARD

class SpecialDeviceComponent(DeviceComponent):

    def set_parameter_controls(self, controls):
        if controls:
            for control in controls:
                control.set_channel(DEVICE_MAP_CHANNEL)
                control.set_light_and_type("Device.On", FADER_TYPE_STANDARD)

        super(SpecialDeviceComponent, self).set_parameter_controls(controls)

    def _update_parameter_controls(self):
        if self._parameter_controls is not None:
            for control in self._parameter_controls:
                control.update()

    def update(self):
        super(SpecialDeviceComponent, self).update()
        if self.is_enabled():
            self._update_parameter_controls()
