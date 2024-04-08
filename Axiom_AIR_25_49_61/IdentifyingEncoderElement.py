# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/IdentifyingEncoderElement.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3839 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.EncoderElement as EncoderElement
from _Framework.InputControlElement import *

class IdentifyingEncoderElement(EncoderElement):

    def __init__(self, msg_type, channel, identifier, map_mode, send_channel=None, identifier_send_offset=0):
        EncoderElement.__init__(self, msg_type, channel, identifier, map_mode)
        self._identify_mode = False
        self._send_channel = send_channel
        self._identifier_send_offset = identifier_send_offset
        self._on_value = 127
        self._off_value = 0
        self._force_next_value = False

    def set_identify_mode(self, identify_mode):
        if self._identify_mode != identify_mode:
            self._identify_mode = identify_mode
            self._request_rebuild()

    def get_identify_mode(self):
        return self._identify_mode

    def install_connections(self, translate_message, install_mapping, install_forwarding):
        current_parameter = self._parameter_to_map_to
        if self._identify_mode:
            self._parameter_to_map_to = None
        InputControlElement.install_connections(self, translate_message, install_mapping, install_forwarding)
        self._parameter_to_map_to = current_parameter
        self._update_led()

    def set_on_off_values(self, on_value, off_value):
        self.clear_send_cache()
        self._on_value = on_value
        self._off_value = off_value

    def set_force_next_value(self):
        self._force_next_value = True

    def turn_on(self):
        self.send_value(self._on_value)

    def turn_off(self):
        self.send_value(self._off_value)

    def reset(self):
        self.send_value(self._off_value)

    def send_valueParse error at or near `LOAD_FAST' instruction at offset 150

    def connect_to(self, parameter):
        if parameter != self._parameter_to_map_to:
            if not self.is_mapped_manually():
                self.send_value((self._off_value), force=True)
        EncoderElement.connect_to(self, parameter)

    def release_parameter(self):
        EncoderElement.release_parameter(self)
        self._update_led()

    def is_mapped_manually(self):
        return not self._is_mapped and not self._is_being_forwarded

    def _update_led(self):
        if self.is_mapped_manually():
            self.send_value((self._on_value), force=True)
        else:
            if self._parameter_to_map_to != None:
                self.send_value((self._on_value), force=True)
            else:
                self.send_value((self._off_value), force=True)