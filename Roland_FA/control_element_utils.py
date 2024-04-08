# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/control_element_utils.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 632 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import depends
from ableton.v2.control_surface import MIDI_CC_TYPE
from ableton.v2.control_surface.elements import ButtonElement, EncoderElement

@depends(skin=None)
def make_button(identifier, name, msg_type=MIDI_CC_TYPE, skin=None):
    return ButtonElement(True, msg_type, 0, identifier, name=name, skin=skin)


def make_encoder(identifier, name):
    return EncoderElement(MIDI_CC_TYPE,
      0, identifier, (Live.MidiMap.MapMode.absolute), name=name)
