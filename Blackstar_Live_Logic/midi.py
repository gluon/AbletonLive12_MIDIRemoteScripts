# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/midi.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 455 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.midi import SYSEX_END, SYSEX_START
SYSEX_HEADER = (
 SYSEX_START, 0, 32, 114)
NUMERIC_DISPLAY_COMMAND = (0, )
LIVE_INTEGRATION_MODE_ID = (
 SYSEX_START,
 0,
 0,
 116,
 1,
 0,
 77,
 67,
 1,
 0,
 7,
 1,
 0)
