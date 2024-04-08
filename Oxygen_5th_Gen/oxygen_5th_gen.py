# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_5th_Gen/oxygen_5th_gen.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 754 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Oxygen_Pro.oxygen_pro import Oxygen_Pro
LIVE_MODE_BYTE = 0

class Oxygen_5th_Gen(Oxygen_Pro):
    live_mode_byte = LIVE_MODE_BYTE
    has_session_component = False

    def __init__(self, *a, **k):
        (super(Oxygen_5th_Gen, self).__init__)(*a, **k)
        self.set_pad_translations(tuple([tuple([col, row, 36 + (3 - row) * 4 + col, 0]) for row in range(3, -1, -1) for col in iter((range(4)))]))
