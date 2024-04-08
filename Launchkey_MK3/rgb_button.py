# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/rgb_button.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1017 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import ButtonElement

class RgbButtonElement(ButtonElement):

    def __init__(self, *a, **k):
        self._led_channel = k.pop("led_channel", 0)
        (super(RgbButtonElement, self).__init__)(*a, **k)

    def _do_send_value(self, value, channel=None):
        super(RgbButtonElement, self)._do_send_value(value, channel=(self._led_channel))
