# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/legacy_bank_definitions.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1948 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Generic.Devices import BANK_NAME_DICT, DEVICE_BOB_DICT, DEVICE_DICT
from ableton.v2.base.collection import IndexedDict
from ..base import memoize
from . import BANK_PARAMETERS_KEY
BEST_OF_PARAMETERS_KEY = "Best of Parameters"

@memoize
def banked():
    return {device_name: IndexedDict([(bank_name, {BANK_PARAMETERS_KEY: parameters}) for bank_name, parameters in zip(bank_names, DEVICE_DICT[device_name])]) for device_name, bank_names in BANK_NAME_DICT.items()}


@memoize
def best_of_banks():
    return {device_name: IndexedDict([(BEST_OF_PARAMETERS_KEY, {BANK_PARAMETERS_KEY: (parameters[0])})]) for device_name, parameters in DEVICE_BOB_DICT.items()}
