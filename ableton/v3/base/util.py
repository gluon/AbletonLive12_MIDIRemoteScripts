# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/base/util.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2731 bytes
from __future__ import absolute_import, print_function, unicode_literals
from . import is_iterable
PITCH_NAMES = ('C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭', 'A', 'A♯/B♭',
               'B')

class CallableBool:

    def __init__(self, value: bool):
        self.value = value

    def __call__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other

    def __bool__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __repr__(self):
        return repr(self.value)


def get_default_ascii_translations():
    ascii_translations = {chr(i): i for i in range(32, 127)}
    ascii_translations["♯"] = 35
    return ascii_translations


DEFAULT_ASCII_TRANSLATIONS = get_default_ascii_translations()

def as_ascii(string, ascii_translations=DEFAULT_ASCII_TRANSLATIONS):
    result = []
    for char in string:
        translated_char = ascii_translations.get(char, ascii_translations["?"])
        if is_iterable(translated_char):
            result.extend(translated_char)
        else:
            result.append(translated_char)

    return result


def hex_to_rgb(hex_value):
    return (
     (hex_value & 16711680) >> 16,
     (hex_value & 65280) >> 8,
     hex_value & 255)


def pitch_index_to_string(index, pitch_names=PITCH_NAMES):
    return pitch_names[index % 12] + str(index // 12 - 2)
