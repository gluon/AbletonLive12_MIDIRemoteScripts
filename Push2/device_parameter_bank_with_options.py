# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/device_parameter_bank_with_options.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1944 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import str
from ableton.v2.base import find_if, listenable_property, liveobj_valid
from ableton.v2.control_surface import DescribedDeviceParameterBank, create_device_bank
from .custom_bank_definitions import OPTIONS_KEY, VIEW_DESCRIPTION_KEY
OPTIONS_PER_BANK = 7

class DescribedDeviceParameterBankWithOptions(DescribedDeviceParameterBank):
    _options = []

    @listenable_property
    def options(self):
        return self._options

    @property
    def bank_view_description(self):
        bank = self._definition.value_by_index(self.index)
        return str(bank.get(VIEW_DESCRIPTION_KEY, ""))

    def _current_option_slots(self):
        bank = self._definition.value_by_index(self.index)
        return bank.get(OPTIONS_KEY) or ('', ) * OPTIONS_PER_BANK

    def _content_slots(self):
        return self._current_option_slots() + super(DescribedDeviceParameterBankWithOptions, self)._content_slots()

    def _collect_options(self):
        option_slots = self._current_option_slots()
        options = getattr(self._device, "options", [])
        return [find_if((lambda o: o.name == str(slot_definition)), options) for slot_definition in option_slots]

    def _update_parameters(self):
        super(DescribedDeviceParameterBankWithOptions, self)._update_parameters()
        self._options = self._collect_options()
        self.notify_options()


def create_device_bank_with_options(device, banking_info):
    if liveobj_valid(device) and banking_info.device_bank_definition(device) is not None:
        bank = DescribedDeviceParameterBankWithOptions(device=device,
          size=8,
          banking_info=banking_info)
    else:
        bank = create_device_bank(device, banking_info)
    return bank
