# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl\TimeDisplay.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)
import Live

from .MackieControlComponent import *


class TimeDisplay(MackieControlComponent):
    def __init__(self, main_script):
        MackieControlComponent.__init__(self, main_script)
        self.__main_script = main_script
        self.__show_beat_time = False
        self.__smpt_format = Live.Song.TimeFormat.smpte_25
        self.__last_send_time = []
        self.show_beats()

    def destroy(self):
        self.clear_display()
        MackieControlComponent.destroy(self)

    def show_beats(self):
        self.__show_beat_time = True
        self.send_midi((NOTE_ON_STATUS, SELECT_BEATS_NOTE, BUTTON_STATE_ON))
        self.send_midi((NOTE_ON_STATUS, SELECT_SMPTE_NOTE, BUTTON_STATE_OFF))

    def show_smpte(self, smpte_mode):
        self.__show_beat_time = False
        self.__smpt_format = smpte_mode
        self.send_midi((NOTE_ON_STATUS, SELECT_BEATS_NOTE, BUTTON_STATE_OFF))
        self.send_midi((NOTE_ON_STATUS, SELECT_SMPTE_NOTE, BUTTON_STATE_ON))

    def toggle_mode(self):
        if self.__show_beat_time:
            self.show_smpte(self.__smpt_format)
        else:
            self.show_beats()

    def clear_display(self):
        time_string = [' ' for i in range(10)]
        self.__send_time_string(time_string, show_points=False)
        self.send_midi((NOTE_ON_STATUS, SELECT_BEATS_NOTE, BUTTON_STATE_OFF))
        self.send_midi((NOTE_ON_STATUS, SELECT_SMPTE_NOTE, BUTTON_STATE_OFF))

    def refresh_state(self):
        self.show_beats()
        self.__last_send_time = []

    def on_update_display_timer(self):
        pass
        pass
        if self.__show_beat_time:
            time_string = str(self.song().get_current_beats_song_time())
        else:
            time_string = str(
                self.song().get_current_smpte_song_time(self.__smpt_format))
        time_string = [c for c in time_string if c not in ['.', ':']]
        if self.__last_send_time != time_string:
            self.__last_send_time = time_string
            self.__send_time_string(time_string, show_points=True)

    def __send_time_string(self, time_string, show_points):
        for c in range(0, 10):
            char = time_string[9 - c].upper()
            char_code = g7_seg_led_conv_table[char]
            if show_points and c in [3, 5, 7]:
                char_code += 64
            self.send_midi((176, 64 + c, char_code))
