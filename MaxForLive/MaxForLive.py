# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MaxForLive/MaxForLive.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2246 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import SimpleControlSurface
from ableton.v2.control_surface.input_control_element import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE, InputControlElement
STATUS_TO_TYPE = {144:MIDI_NOTE_TYPE, 
 176:MIDI_CC_TYPE,  224:MIDI_PB_TYPE}

class MaxForLive(SimpleControlSurface):

    def __init__(self, *a, **k):
        (super(MaxForLive, self).__init__)(*a, **k)
        self._registered_control_names = []
        self._registered_messages = []

    def register_midi_controlParse error at or near `COME_FROM' instruction at offset 70_0