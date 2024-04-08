# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/midi.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1299 bytes
from __future__ import absolute_import, print_function, unicode_literals
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
M_AUDIO_MANUFACTURER_ID = (0, 1, 5)
SYSEX_HEADER = (
 SYSEX_START_BYTE,) + M_AUDIO_MANUFACTURER_ID + (127, 0, 0)
LED_CONTROL_BYTES = (107, 0, 1)
LED_ENABLE_BYTE = 1
LED_MODE_BYTES = (108, 0, 1)
FIRMWARE_CONTROL_BYTE = 0
SOFTWARE_CONTROL_BYTE = 3
FIRMWARE_MODE_BYTES = (109, 0, 1)
LIVE_MODE_BYTE = 2
CONTROL_MODE_BYTES = (110, 0, 1)
RECORD_MODE_BYTE = 2
DEVICE_MODE_BYTE = 7
