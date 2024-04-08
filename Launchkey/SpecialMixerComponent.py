# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey/SpecialMixerComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2538 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import _Framework.MixerComponent as MixerComponent

class SpecialMixerComponent(MixerComponent):

    def __init__(self, num_tracks):
        MixerComponent.__init__(self, num_tracks)
        self._strip_mute_solo_buttons = None
        self._mute_solo_flip_button = None
        self._mute_solo_is_flipped = False

    def disconnect(self):
        MixerComponent.disconnect(self)
        if self._mute_solo_flip_button != None:
            self._mute_solo_flip_button.remove_value_listener(self._mute_solo_flip_value)
            self._mute_solo_flip_button = None
        self._strip_mute_solo_buttons = None

    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)

    def set_strip_mute_solo_buttons(self, buttons, flip_button):
        if self._mute_solo_flip_button != None:
            self._mute_solo_flip_button.remove_value_listener(self._mute_solo_flip_value)
        self._mute_solo_flip_button = flip_button
        if self._mute_solo_flip_button != None:
            self._mute_solo_flip_button.add_value_listener(self._mute_solo_flip_value)
        self._strip_mute_solo_buttons = buttons
        for index in range(len(self._channel_strips)):
            strip = self.channel_strip(index)
            button = None
            if self._strip_mute_solo_buttons != None:
                button = self._strip_mute_solo_buttons[index]
            strip.set_mute_button(button)
            strip.set_solo_button(None)

    def _mute_solo_flip_value(self, value):
        if self._strip_mute_solo_buttons != None:
            if value == 0:
                self._mute_solo_is_flipped = not self._mute_solo_is_flipped
                self._mute_solo_flip_button.turn_on() if self._mute_solo_is_flipped else self._mute_solo_flip_button.turn_off()
                for index in range(len(self._strip_mute_solo_buttons)):
                    strip = self.channel_strip(index)
                    if self._mute_solo_is_flipped:
                        strip.set_mute_button(None)
                        strip.set_solo_button(self._strip_mute_solo_buttons[index])
                    else:
                        strip.set_solo_button(None)
                        strip.set_mute_button(self._strip_mute_solo_buttons[index])
