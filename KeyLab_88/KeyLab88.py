# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_88/KeyLab88.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 862 bytes
from __future__ import absolute_import, print_function, unicode_literals
import KeyLab.KeyLab as KeyLab

class KeyLab88(KeyLab):

    def _setup_hardware_encoder(self, hardware_id, identifier, channel=0):
        self._set_encoder_cc_msg_type(hardware_id)
        self._set_identifier(hardware_id, identifier)
        self._set_channel(hardware_id, channel)
        self._set_binary_offset_mode(hardware_id)

    def _setup_hardware_button(self, hardware_id, identifier, channel=0, **k):
        self._set_button_msg_type(hardware_id, "cc")
        self._set_channel(hardware_id, channel)
        self._set_identifier(hardware_id, identifier)
        self._set_value_minimum(hardware_id)
        self._set_value_maximum(hardware_id)
        self._set_momentary_mode(hardware_id, is_momentary=True)
