# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/SpecialMixerComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1475 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import _Framework.MixerComponent as MixerComponent
from .DisplayingChanStripComponent import DisplayingChanStripComponent

class SpecialMixerComponent(MixerComponent):

    def __init__(self, name_display, value_display, num_tracks, num_returns=0):
        MixerComponent.__init__(self, num_tracks, num_returns=0)
        self._name_display = name_display
        self._value_display = value_display
        for index in range(num_tracks):
            self._channel_strips[index].set_name_display(self._name_display)
            self._channel_strips[index].set_value_display(self._value_display)

        for index in range(num_returns):
            self._return_strips[index].set_name_display(self._name_display)
            self._return_strips[index].set_value_display(self._value_display)

        self._selected_strip.set_name_display(self._name_display)
        self._selected_strip.set_value_display(self._value_display)

    def disconnect(self):
        MixerComponent.disconnect(self)
        self._name_display = None
        self._value_display = None

    def tracks_to_use(self):
        return self.song().visible_tracks + self.song().return_tracks

    def _create_strip(self):
        return DisplayingChanStripComponent()
