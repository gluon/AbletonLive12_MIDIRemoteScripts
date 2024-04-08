# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/SpecialSessionComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1559 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.SessionComponent as SessionComponent

class SpecialSessionComponent(SessionComponent):

    def _update_stop_clips_led(self, index):
        if self.is_enabled():
            if self._stop_track_clip_buttons != None:
                if index < len(self._stop_track_clip_buttons):
                    button = self._stop_track_clip_buttons[index]
                    tracks_to_use = self.tracks_to_use()
                    track_index = index + self.track_offset()
                    if 0 <= track_index < len(tracks_to_use):
                        track = tracks_to_use[track_index]
                        if track.fired_slot_index == -2:
                            button.send_value(self._stop_clip_triggered_value)
                        elif track.playing_slot_index >= 0:
                            button.send_value(self._stop_clip_value)
                        else:
                            button.turn_off()
                    else:
                        button.send_value(4)
