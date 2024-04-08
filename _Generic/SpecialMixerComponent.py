# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/SpecialMixerComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 661 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.MixerComponent as MixerComponent
from .SelectChanStripComponent import SelectChanStripComponent

class SpecialMixerComponent(MixerComponent):

    def _create_strip(self):
        return SelectChanStripComponent()

    def set_bank_up_button(self, button):
        self.set_bank_buttons(button, self._bank_down_button)

    def set_bank_down_button(self, button):
        self.set_bank_buttons(self._bank_up_button, button)
