# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/hardware_settings.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 829 bytes
from __future__ import absolute_import, print_function, unicode_literals
from KeyLab_Essential import sysex
from KeyLab_Essential.hardware_settings import HardwareSettingsComponent as HardwareSettingsComponentBase

class HardwareSettingsComponent(HardwareSettingsComponentBase):

    def __init__(self, *a, **k):
        (super(HardwareSettingsComponent, self).__init__)(*a, **k)
        self._vegas_mode_switch = None

    def set_vegas_mode_switch(self, switch):
        self._vegas_mode_switch = switch

    def set_hardware_live_mode_enabled(self, enable):
        super(HardwareSettingsComponent, self).set_hardware_live_mode_enabled(enable)
        if enable:
            if self._vegas_mode_switch:
                self._vegas_mode_switch.send_value(sysex.OFF_VALUE)
