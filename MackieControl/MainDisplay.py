# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl\MainDisplay.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)
from ableton.v3.base import as_ascii
from .MackieControlComponent import *

class MainDisplay(MackieControlComponent):
    pass

    def __init__(self, main_script):
        MackieControlComponent.__init__(self, main_script)
        self.__stack_offset = 0
        self.__last_send_messages = [[], []]

    def destroy(self):
        NUM_CHARS_PER_DISPLAY_LINE = 54
        upper_message = 'Ableton Live'.center(NUM_CHARS_PER_DISPLAY_LINE)
        self.send_display_string(upper_message, 0, 0)
        lower_message = 'Device is offline'.center(NUM_CHARS_PER_DISPLAY_LINE)
        self.send_display_string(lower_message, 1, 0)
        MackieControlComponent.destroy(self)

    def stack_offset(self):
        return self.__stack_offset

    def set_stack_offset(self, offset):
        pass
        self.__stack_offset = offset

    def send_display_string(self, display_string, display_row, cursor_offset):
        if display_row == 0:
            offset = cursor_offset
        elif display_row == 1:
            offset = NUM_CHARS_PER_DISPLAY_LINE + 2 + cursor_offset
        message_string = as_ascii(display_string)
        if self.__last_send_messages[display_row] != message_string:
            self.__last_send_messages[display_row] = message_string
            if self.main_script().is_extension():
                device_type = SYSEX_DEVICE_TYPE_XT
            else:
                device_type = SYSEX_DEVICE_TYPE
            display_sysex = (240, 0, 0, 102, device_type, 18, offset) + tuple(message_string) + (247,)
            self.send_midi(display_sysex)

    def refresh_state(self):
        self.__last_send_messages = [[], []]

    def on_update_display_timer(self):
        return