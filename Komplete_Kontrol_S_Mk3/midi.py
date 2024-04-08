# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/midi.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1056 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.midi import SYSEX_START
MIDI_CHANNEL = 15
SYSEX_HEADER = (
 SYSEX_START, 0, 33, 9, 0, 0, 68, 67, 1, 0)
FOCUS_FOLLOW_HEADER = SYSEX_HEADER + (65, 0, 0)
TRACK_TYPE_HEADER = SYSEX_HEADER + (64, )
TRACK_SELECT_HEADER = SYSEX_HEADER + (66, )
TRACK_MUTE_HEADER = SYSEX_HEADER + (67, )
TRACK_SOLO_HEADER = SYSEX_HEADER + (68, )
TRACK_ARM_HEADER = SYSEX_HEADER + (69, )
TRACK_VOLUME_HEADER = SYSEX_HEADER + (70, 0)
TRACK_PAN_HEADER = SYSEX_HEADER + (71, 0)
TRACK_NAME_HEADER = SYSEX_HEADER + (72, 0)
TRACK_METER_HEADER = SYSEX_HEADER + (73, 2, 0)
TRACK_MUTE_VIA_SOLO_HEADER = SYSEX_HEADER + (74, )
DEFAULT_TRACK_TYPE = 1
MASTER_TRACK_TYPE = 6
