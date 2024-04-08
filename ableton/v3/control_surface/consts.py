# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/consts.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 771 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DEFAULT_PRIORITY
LOW_PRIORITY = DEFAULT_PRIORITY - 1
HIGH_PRIORITY = DEFAULT_PRIORITY + 1
M4L_PRIORITY = HIGH_PRIORITY + 1
MOMENTARY_DELAY = 0.3
ACTIVE_PARAMETER_TIMEOUT = 0.75
