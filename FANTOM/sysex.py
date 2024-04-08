# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FANTOM/sysex.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1245 bytes
from __future__ import absolute_import, print_function, unicode_literals
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
HEADER = (
 SYSEX_START_BYTE, 65, 16, 0, 0, 0, 91)
INITIATE_CONNECTION = HEADER + (18, 14, 80, 0, 1, SYSEX_END_BYTE)
TERMINATE_CONNECTION = HEADER + (18, 14, 80, 0, 0, SYSEX_END_BYTE)
TRACK_INFO_DISPLAY_HEADER = HEADER + (18, 14, 80, 1, 0)
SCENE_NAME_DISPLAY_HEADER = HEADER + (18, 14, 80, 2, 0)
BEAT_TIME_DISPLAY_HEADER = HEADER + (18, 14, 80, 3, 0)
TEMPO_DISPLAY_HEADER = HEADER + (18, 14, 80, 3, 1)
REFRESH_REQUEST = HEADER + (17, 14)
NAME_LENGTH = 8
NAME_TERMINATOR = 0
