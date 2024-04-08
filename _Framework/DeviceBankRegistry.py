# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/DeviceBankRegistry.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1577 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .SubjectSlot import Subject

class DeviceBankRegistry(Subject):
    __subject_events__ = ('device_bank', )

    def __init__(self, *a, **k):
        (super(DeviceBankRegistry, self).__init__)(*a, **k)
        self._device_bank_registry = {}
        self._device_bank_listeners = []

    def compact_registry(self):
        newreg = dict([k__ for k__ in list(self._device_bank_registry.items()) if k__[0] != None])
        self._device_bank_registry = newreg

    def set_device_bank(self, device, bank):
        key = self._find_device_bank_key(device) or device
        old = self._device_bank_registry[key] if key in self._device_bank_registry else 0
        if old != bank:
            self._device_bank_registry[key] = bank
            self.notify_device_bank(device, bank)

    def get_device_bank(self, device):
        return self._device_bank_registry.get(self._find_device_bank_key(device), 0)

    def _find_device_bank_key(self, device):
        for k in self._device_bank_registry.keys():
            if k == device:
                return k
