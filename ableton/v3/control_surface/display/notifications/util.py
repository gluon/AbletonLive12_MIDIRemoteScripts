# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/util.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 597 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from typing_extensions import LiteralString
else:
    LiteralString = str

def toggle_text_generator(format_string: "LiteralString") -> "Callable[[bool], str]":

    def notification_fn(is_on):
        return format_string.format("on" if is_on else "off")

    return notification_fn
