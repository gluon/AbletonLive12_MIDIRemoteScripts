# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/display_data_source.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3494 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial

def adjust_string_crop(original, length):
    length = int(length)
    return original[None[:length]].ljust(length)


def adjust_string(original, length):
    length = int(length)
    resulting_string = original
    if len(resulting_string) > length:
        unit_db = resulting_string.endswith("dB") and resulting_string.find(".") != -1
        if len(resulting_string.strip()) > length:
            if unit_db:
                resulting_string = resulting_string[None[:-2]]
        if len(resulting_string) > length:
            for char in (' ', '_', 'i', 'o', 'u', 'e', 'a'):
                offset = 0 if char == " " else 1
                while len(resulting_string) > length and resulting_string.rfind(char, offset) > 0:
                    char_pos = resulting_string.rfind(char, offset)
                    resulting_string = resulting_string[None[:char_pos]] + resulting_string[(char_pos + 1)[:None]]

            resulting_string = resulting_string[None[:length]]
    if len(resulting_string) < length:
        resulting_string = resulting_string.ljust(length)
    return resulting_string


class DisplayDataSource(object):
    _separator = ""
    _adjust_string_fn = partial(adjust_string)

    def __init__(self, display_string="", separator=None, adjust_string_fn=adjust_string, *a, **k):
        (super(DisplayDataSource, self).__init__)(*a, **k)
        if adjust_string_fn is not None:
            self._adjust_string_fn = partial(adjust_string_fn)
        if separator is not None:
            self._separator = separator
        self._display_string = display_string
        self._update_callback = None
        self._in_update = False

    @property
    def separator(self):
        return self._separator

    @separator.setter
    def separator(self, separator):
        if separator != self._separator:
            self._separator = separator
            self.update()

    def set_update_callback(self, update_callback):
        self._update_callback = update_callback
        if update_callback:
            self.update()

    def set_display_string(self, new_string):
        if self._display_string != new_string:
            self._display_string = new_string
            self.update()

    def clear(self):
        self.set_display_string("")
        self.separator = ""

    def update(self):
        self._in_update = True
        if self._update_callback is not None:
            self._update_callback()
        self._in_update = False

    def display_string(self):
        return self._display_string

    def adjust_string(self, width):
        return self._adjust_string_fn(self.display_string(), width)
