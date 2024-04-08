# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro_Mini/simple_device.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1197 bytes
from __future__ import absolute_import, print_function, unicode_literals
from novation.simple_device import SimpleDeviceParameterComponent as SimpleDeviceParameterComponentBase
NUM_CONTROLS = 4

class SimpleDeviceParameterComponent(SimpleDeviceParameterComponentBase):

    def __init__(self, *a, **k):
        (super(SimpleDeviceParameterComponent, self).__init__)(*a, **k)
        self._parameter_offset = 0

    def toggle_parameter_offset(self):
        self._parameter_offset = NUM_CONTROLS - self._parameter_offset
        self.update()

    @SimpleDeviceParameterComponentBase.selected_bank.getter
    def selected_bank(self):
        bank = self._banks[0] or []
        if self._parameter_offset:
            if len(bank) > self._parameter_offset:
                offset_bank = bank[self._parameter_offset[:None]]
                if any(offset_bank):
                    return offset_bank
        return bank
