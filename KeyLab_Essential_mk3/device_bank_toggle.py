# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential_mk3/device_bank_toggle.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1574 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listenable_property
from ableton.v3.control_surface.components import DeviceBankNavigationComponent
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable

class DeviceBankToggleComponent(DeviceBankNavigationComponent, Renderable):
    bank_index = listenable_property.managed(0)
    has_changed_bank_index = listenable_property.managed(False)
    bank_toggle_button = ButtonControl()

    def set_bank_toggle_button(self, button):
        self.bank_toggle_button.set_control_element(button)

    @bank_toggle_button.pressed
    def bank_toggle_button(self, _):
        self._bank_provider.index = 2 if self._bank_provider.index == 0 else 0
        self.has_changed_bank_index = True

    def update(self):
        super().update()
        can_bank = self._bank_provider is not None and self._adjusted_bank_count() > 1
        self.bank_index = self._bank_provider.index if can_bank else 0
        self.bank_toggle_button.enabled = can_bank
        if can_bank:
            self.bank_toggle_button.color = "Banking.PageOne" if self._bank_provider.index == 0 else "Banking.PageTwo"
