# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyPad/CombinedButtonsElement.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1348 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import OFF_VALUE
import _Framework.ButtonMatrixElement as ButtonMatrixElement
from _Framework.Util import BooleanContext, const

class CombinedButtonsElement(ButtonMatrixElement):

    def __init__(self, buttons=None, *a, **k):
        (super(CombinedButtonsElement, self).__init__)(a, rows=[buttons], **k)
        self._is_pressed = BooleanContext(False)

    def is_momentary(self):
        return True

    def is_pressed(self):
        return any(map((lambda b__:         if b__[0] is not None:
b__[0].is_pressed() # Avoid dead code: False), self.iterbuttons())) or bool(self._is_pressed)

    def on_nested_control_element_value(self, value, sender):
        with self._is_pressed():
            self.notify_value(value)
        if value != OFF_VALUE:
            if not getattr(sender, "is_momentary", const(False))():
                self.notify_value(OFF_VALUE)

    def send_value(self, value):
        for button, _ in self.iterbuttons():
            if button:
                button.send_value(value)

    def set_light(self, value):
        for button, _ in self.iterbuttons():
            if button:
                button.set_light(value)
