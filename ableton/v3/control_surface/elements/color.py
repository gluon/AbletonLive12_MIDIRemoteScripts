# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/color.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 3823 bytes
from __future__ import absolute_import, print_function, unicode_literals
from abc import ABC, abstractmethod
from typing import NamedTuple, Optional
from ...base import memoize, old_hasattr

@memoize
def create_rgb_color(values):
    if values is not None:
        return RgbColor(*values)


class Color(ABC):

    @abstractmethod
    def draw(self, interface):
        pass

    @property
    def midi_value(self):
        raise NotImplementedError


class SimpleColor(Color):

    def __init__(self, value, channel=None, *a, **k):
        (super().__init__)(*a, **k)
        self._value = value
        self._channel = channel

    @property
    def midi_value(self):
        return self._value

    def draw(self, interface):
        interface.send_value((self._value), channel=(self._channel))


class RgbColor(Color):

    def __init__(self, *values, **k):
        (super().__init__)(**k)
        self._values = values

    def draw(self, interface):
        (interface.send_value)(*self._values)


class ColorPart(NamedTuple):
    value: int
    channel = None
    channel: Optional[int]


class ComplexColor(Color):

    def __init__(self, color_parts, *a, **k):
        (super().__init__)(*a, **k)
        self._color_parts = color_parts

    def draw(self, interface):
        for part in self._color_parts:
            interface.send_value((part.value), channel=(part.channel))


class FallbackColor(Color):

    def __init__(self, rgb_color, fallback_color):
        self._rgb_color = rgb_color
        self._fallback_color = fallback_color

    @property
    def midi_value(self):
        return self._rgb_color.midi_value

    def draw(self, interface):
        if old_hasattr(interface, "is_rgb") and interface.is_rgb:
            self._rgb_color.draw(interface)
        else:
            self._fallback_color.draw(interface)
