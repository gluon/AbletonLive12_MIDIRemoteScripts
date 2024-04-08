# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/mode_collector.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1782 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, listenable_property, listens

class ModeCollector(EventObject):

    def __init__(self, main_modes=None, mix_modes=None, global_mix_modes=None, device_modes=None, *a, **k):
        (super(ModeCollector, self).__init__)(*a, **k)
        self._main_modes = main_modes
        self._mix_modes = mix_modes
        self._global_mix_modes = global_mix_modes
        self._device_modes = device_modes
        self._on_selected_main_mode_changed.subject = main_modes
        self._on_selected_mix_mode_changed.subject = mix_modes
        self._on_selected_global_mix_mode_changed.subject = global_mix_modes
        self._on_selected_device_mode_changed.subject = device_modes

    @listenable_property
    def main_mode(self):
        return self._main_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_main_mode_changed(self, mode):
        self.notify_main_mode()

    @listenable_property
    def mix_mode(self):
        return self._mix_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_mix_mode_changed(self, mode):
        self.notify_mix_mode()

    @listenable_property
    def global_mix_mode(self):
        return self._global_mix_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_global_mix_mode_changed(self, mode):
        self.notify_global_mix_mode()

    @listenable_property
    def device_mode(self):
        return self._device_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_device_mode_changed(self, mode):
        self.notify_device_mode()
