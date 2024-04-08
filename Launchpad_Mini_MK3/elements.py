# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Mini_MK3/elements.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1283 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import depends
from ableton.v2.control_surface.elements import ColorSysexElement
from novation import sysex
from novation.launchpad_elements import LaunchpadElements, create_button
from . import sysex_ids as ids

class Elements(LaunchpadElements):
    model_id = ids.LP_MINI_MK3_ID
    default_layout = sysex.KEYS_LAYOUT_BYTE

    @depends(skin=None)
    def __init__(self, skin=None, *a, **k):
        (super(Elements, self).__init__)(*a, **k)
        self.drums_mode_button = create_button(96, "Drums_Mode_Button")
        self.keys_mode_button = create_button(97, "Keys_Mode_Button")
        self.user_mode_button = create_button(98, "User_Mode_Button")
        session_button_color_identifier = sysex.STD_MSG_HEADER + (
         ids.LP_MINI_MK3_ID,
         20)
        self.session_button_color_element = ColorSysexElement(name="Session_Button_Color_Element",
          sysex_identifier=session_button_color_identifier,
          send_message_generator=(lambda v: session_button_color_identifier + v + (sysex.SYSEX_END_BYTE,)),
          skin=skin)
