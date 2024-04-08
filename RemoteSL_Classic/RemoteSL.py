# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/RemoteSL_Classic/RemoteSL.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 11252 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, str
import Live, MidiRemoteScript
from _Generic.util import DeviceAppointer
from .consts import *
from .DisplayController import DisplayController
from .EffectController import EffectController
from .MixerController import MixerController

class RemoteSL(object):

    def __init__(self, c_instance):
        self._RemoteSL__c_instance = c_instance
        self._RemoteSL__automap_has_control = False
        self._RemoteSL__display_controller = DisplayController(self)
        self._RemoteSL__effect_controller = EffectController(self, self._RemoteSL__display_controller)
        self._RemoteSL__mixer_controller = MixerController(self, self._RemoteSL__display_controller)
        self._RemoteSL__components = [
         self._RemoteSL__effect_controller,
         self._RemoteSL__mixer_controller,
         self._RemoteSL__display_controller]
        self._RemoteSL__update_hardware_delay = -1
        self._device_appointer = DeviceAppointer(song=(self.song()),
          appointed_device_setter=(self._set_appointed_device))

    def disconnect(self):
        for c in self._RemoteSL__components:
            c.disconnect()

        self._device_appointer.disconnect()
        self.send_midi(ALL_LEDS_OFF_MESSAGE)
        self.send_midi(GOOD_BYE_SYSEX_MESSAGE)

    def application(self):
        return Live.Application.get_application()

    def song(self):
        return self._RemoteSL__c_instance.song()

    def suggest_input_port(self):
        return "RemoteSL"

    def suggest_output_port(self):
        return "RemoteSL"

    def can_lock_to_devices(self):
        return True

    def lock_to_device(self, device):
        self._RemoteSL__effect_controller.lock_to_device(device)

    def unlock_from_device(self, device):
        self._RemoteSL__effect_controller.unlock_from_device(device)

    def _set_appointed_device(self, device):
        self._RemoteSL__effect_controller.set_appointed_device(device)

    def toggle_lock(self):
        self._RemoteSL__c_instance.toggle_lock()

    def suggest_map_mode(self, cc_no, channel):
        result = Live.MidiMap.MapMode.absolute
        if cc_no in fx_encoder_row_ccs:
            result = Live.MidiMap.MapMode.relative_smooth_signed_bit
        return result

    def restore_bank(self, bank):
        self._RemoteSL__effect_controller.restore_bank(bank)

    def supports_pad_translation(self):
        return True

    def show_message(self, message):
        self._RemoteSL__c_instance.show_message(message)

    def instance_identifier(self):
        return self._RemoteSL__c_instance.instance_identifier()

    def connect_script_instances(self, instanciated_scripts):
        pass

    def request_rebuild_midi_map(self):
        self._RemoteSL__c_instance.request_rebuild_midi_map()

    def send_midi(self, midi_event_bytes):
        if not self._RemoteSL__automap_has_control:
            self._RemoteSL__c_instance.send_midi(midi_event_bytes)

    def refresh_state(self):
        self._RemoteSL__update_hardware_delay = 5

    def __update_hardware(self):
        self._RemoteSL__automap_has_control = False
        self.send_midi(WELCOME_SYSEX_MESSAGE)
        for c in self._RemoteSL__components:
            c.refresh_state()

    def build_midi_map(self, midi_map_handle):
        if not self._RemoteSL__automap_has_control:
            for c in self._RemoteSL__components:
                c.build_midi_map(self._RemoteSL__c_instance.handle(), midi_map_handle)

        self._RemoteSL__c_instance.set_pad_translation(PAD_TRANSLATION)

    def update_display(self):
        if self._RemoteSL__update_hardware_delay > 0:
            self._RemoteSL__update_hardware_delay -= 1
            if self._RemoteSL__update_hardware_delay == 0:
                self._RemoteSL__update_hardware()
                self._RemoteSL__update_hardware_delay = -1
        for c in self._RemoteSL__components:
            c.update_display()

    def receive_midiParse error at or near `COME_FROM' instruction at offset 382_0