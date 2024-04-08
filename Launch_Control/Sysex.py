# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/Sysex.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 496 bytes
from __future__ import absolute_import, print_function, unicode_literals
MODE_CHANGE_PREFIX = (240, 0, 32, 41, 2, 10, 119)
MIXER_MODE = (240, 0, 32, 41, 2, 10, 119, 8, 247)
SESSION_MODE = (240, 0, 32, 41, 2, 10, 119, 9, 247)
DEVICE_MODE = (240, 0, 32, 41, 2, 10, 119, 10, 247)

def make_automatic_flashing_message(channel):
    return (
     176 + channel, 0, 40)
