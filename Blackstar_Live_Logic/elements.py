# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/elements.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1406 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import MIDI_CC_TYPE
from ableton.v2.control_surface.elements import ButtonElement, ButtonMatrixElement, SysexElement
from ableton.v2.control_surface.midi import SYSEX_END
from .midi import LIVE_INTEGRATION_MODE_ID, NUMERIC_DISPLAY_COMMAND, SYSEX_HEADER
from .skin import skin
from .time_display import TimeDisplayElement
NUM_LOOPER_SWITCHES = 6

def create_button(identifier, name, msg_type=MIDI_CC_TYPE, **k):
    return ButtonElement(True, msg_type, 15, identifier, skin=skin, name=name, **k)


class Elements(object):

    def __init__(self, *a, **k):
        (super(Elements, self).__init__)(*a, **k)
        self.foot_switches = ButtonMatrixElement(rows=[
         [create_button(i, "Foot_Switch_{}".format(i)) for i in range(NUM_LOOPER_SWITCHES)]],
          name="Foot_Switches")
        self.time_display = TimeDisplayElement(SYSEX_HEADER + NUMERIC_DISPLAY_COMMAND, (SYSEX_END,))
        self.live_integration_mode_switch = SysexElement(name="Live_Integration_Mode_Switch",
          send_message_generator=(lambda v: LIVE_INTEGRATION_MODE_ID + (v, SYSEX_END)))
