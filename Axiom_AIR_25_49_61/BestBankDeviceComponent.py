# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/BestBankDeviceComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2411 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Generic.Devices import BANK_NAME_DICT, DEVICE_BOB_DICT, DEVICE_DICT, parameter_bank_names, parameter_banks
import _Framework.DeviceComponent as DeviceComponent
BOP_BANK_NAME = "Best of Parameters"

class BestBankDeviceComponent(DeviceComponent):

    def __init__(self, *a, **k):
        (super(BestBankDeviceComponent, self).__init__)(*a, **k)
        new_banks = {}
        new_bank_names = {}
        self._device_banks = DEVICE_DICT
        self._device_bank_names = BANK_NAME_DICT
        self._device_best_banks = DEVICE_BOB_DICT
        for device_name in list(self._device_banks.keys()):
            current_banks = self._device_banks[device_name]
            if len(current_banks) > 1:
                current_banks = self._device_best_banks[device_name] + current_banks
                new_bank_names[device_name] = (BOP_BANK_NAME,) + self._device_bank_names[device_name]
            new_banks[device_name] = current_banks

        self._device_banks = new_banks
        self._device_bank_names = new_bank_names

    def set_parameter_controls(self, controls):
        if self._parameter_controls != None:
            for control in self._parameter_controls:
                if self._device != None:
                    control.release_parameter()

        self._parameter_controls = controls
        self.update()

    def _number_of_parameter_banks(self):
        result = 0
        if self._device != None:
            if self._device.class_name in list(self._device_banks.keys()):
                result = len(self._device_banks[self._device.class_name])
            else:
                result = DeviceComponent._number_of_parameter_banks(self)
        return result

    def _parameter_banks(self):
        return parameter_banks(self._device, self._device_banks)

    def _parameter_bank_names(self):
        return parameter_bank_names(self._device, self._device_bank_names)

    def _is_banking_enabled(self):
        return True
