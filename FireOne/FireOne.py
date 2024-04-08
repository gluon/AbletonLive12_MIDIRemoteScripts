# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FireOne/FireOne.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 14469 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range, str
import Live, MidiRemoteScript
from ableton.v2.base import move_current_song_time
NOTE_OFF_STATUS = 128
NOTE_ON_STATUS = 144
CC_STATUS = 176
NUM_NOTES = 128
NUM_CC_NO = 128
NUM_CHANNELS = 16
JOG_DIAL_CC = 60
RWD_NOTE = 91
FFWD_NOTE = 92
STOP_NOTE = 93
PLAY_NOTE = 94
REC_NOTE = 95
SHIFT_NOTE = 70
FIRE_ONE_TRANSPORT = [
 RWD_NOTE, FFWD_NOTE, STOP_NOTE, PLAY_NOTE, REC_NOTE]
FIRE_ONE_F_KEYS = list(range(54, 64))
FIRE_ONE_CHANNEL = 0

class FireOne(object):

    def __init__(self, c_instance):
        self._FireOne__c_instance = c_instance
        self._FireOne__shift_pressed = False
        self._FireOne__rwd_pressed = False
        self._FireOne__ffwd_pressed = False
        self._FireOne__jog_dial_map_mode = Live.MidiMap.MapMode.absolute
        self._FireOne__spooling_counter = 0
        self.song().add_is_playing_listener(self._FireOne__playing_status_changed)
        self.song().add_record_mode_listener(self._FireOne__recording_status_changed)
        self.song().add_visible_tracks_listener(self._FireOne__tracks_changed)
        self._FireOne__playing_status_changed()
        self._FireOne__recording_status_changed()

    def application(self):
        return Live.Application.get_application()

    def song(self):
        return self._FireOne__c_instance.song()

    def disconnect(self):
        self.send_midi((NOTE_OFF_STATUS + FIRE_ONE_CHANNEL, PLAY_NOTE, 0))
        self.send_midi((NOTE_OFF_STATUS + FIRE_ONE_CHANNEL, REC_NOTE, 0))
        self.song().remove_is_playing_listener(self._FireOne__playing_status_changed)
        self.song().remove_record_mode_listener(self._FireOne__recording_status_changed)
        self.song().remove_visible_tracks_listener(self._FireOne__tracks_changed)

    def connect_script_instances(self, instanciated_scripts):
        pass

    def suggest_input_port(self):
        return str("FireOne Control")

    def suggest_output_port(self):
        return str("FireOne Control")

    def suggest_map_mode(self, cc_no, channel):
        suggested_map_mode = Live.MidiMap.MapMode.absolute
        if cc_no == JOG_DIAL_CC:
            suggested_map_mode = self._FireOne__jog_dial_map_mode
        return suggested_map_mode

    def can_lock_to_devices(self):
        return False

    def request_rebuild_midi_map(self):
        self._FireOne__c_instance.request_rebuild_midi_map()

    def send_midi(self, midi_event_bytes):
        self._FireOne__c_instance.send_midi(midi_event_bytes)

    def refresh_state(self):
        pass

    def build_midi_map(self, midi_map_handle):
        script_handle = self._FireOne__c_instance.handle()
        Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, FIRE_ONE_CHANNEL, JOG_DIAL_CC)
        for note in FIRE_ONE_TRANSPORT:
            Live.MidiMap.forward_midi_note(script_handle, midi_map_handle, FIRE_ONE_CHANNEL, note)

        Live.MidiMap.forward_midi_note(script_handle, midi_map_handle, FIRE_ONE_CHANNEL, SHIFT_NOTE)
        for index in range(len(self.song().visible_tracks)):
            if len(FIRE_ONE_F_KEYS) > index:
                Live.MidiMap.forward_midi_note(script_handle, midi_map_handle, FIRE_ONE_CHANNEL, FIRE_ONE_F_KEYS[index])
            else:
                break

    def update_display(self):
        if self._FireOne__ffwd_pressed:
            self._FireOne__spooling_counter += 1
            if self._FireOne__spooling_counter % 2 == 0:
                self.song().jump_by(self.song().signature_denominator)
        elif self._FireOne__rwd_pressed:
            self._FireOne__spooling_counter += 1
            if self._FireOne__spooling_counter % 2 == 0:
                self.song().jump_by(-1 * self.song().signature_denominator)

    def receive_midi(self, midi_bytes):
        cc_or_note = midi_bytes[1]
        if midi_bytes[0] & 240 == CC_STATUS:
            if cc_or_note is JOG_DIAL_CC:
                self._FireOne__jog_dial_message(cc_or_note, midi_bytes[2])
        elif midi_bytes[0] & 240 in (NOTE_ON_STATUS, NOTE_OFF_STATUS):
            value = midi_bytes[2]
            if midi_bytes[0] & 240 == NOTE_OFF_STATUS:
                value = 0
            elif cc_or_note is SHIFT_NOTE:
                self._FireOne__shift_pressed = value != 0
            else:
                if cc_or_note in FIRE_ONE_TRANSPORT:
                    self._FireOne__transport_message(cc_or_note, value)
                else:
                    if cc_or_note in FIRE_ONE_F_KEYS:
                        self._FireOne__f_key_message(cc_or_note, value)

    def __playing_status_changed(self):
        status = NOTE_OFF_STATUS
        note = PLAY_NOTE
        value = 0
        if self.song().is_playing:
            status = NOTE_ON_STATUS
            value = 127
        status += FIRE_ONE_CHANNEL
        self.send_midi((status, note, value))

    def __recording_status_changed(self):
        status = NOTE_OFF_STATUS
        note = REC_NOTE
        value = 0
        if self.song().record_mode:
            status = NOTE_ON_STATUS
            value = 127
        status += FIRE_ONE_CHANNEL
        self.send_midi((status, note, value))

    def __tracks_changed(self):
        self.request_rebuild_midi_map()

    def __transport_messageParse error at or near `COME_FROM' instruction at offset 300_0

    def __jog_dial_message(self, cc_no, cc_value):
        moved_forward = cc_value in range(1, 64)
        if (self._FireOne__shift_pressed or self.application().view.is_view_visible)("Session"):
            index = list(self.song().scenes).index(self.song().view.selected_scene)
            if moved_forward:
                if index < len(self.song().scenes) - 1:
                    index = index + 1
                else:
                    if index > 0:
                        index = index - 1
                self.song().view.selected_scene = self.song().scenes[index]
            else:
                value = cc_value
                if not moved_forward:
                    value -= 64
                    value *= -1
                move_current_song_time(self.song(), value)
        elif self.application().view.is_view_visible("Session"):
            tracks = self.song().visible_tracks
            index = list(tracks).index(self.song().view.selected_track)
            if moved_forward:
                if index < len(tracks) - 1:
                    index = index + 1
            elif index > 0:
                index = index - 1
            self.song().view.selected_track = tracks[index]
        else:
            value = cc_value
            if not moved_forward:
                value -= 64
                value *= -0.1
            self.song().tempo = self.song().tempo + 0.1 * value

    def __f_key_message(self, f_key, value):
        index = list(FIRE_ONE_F_KEYS).index(f_key)
        tracks = self.song().visible_tracks
        track = tracks[index]
        if value > 0:
            if self._FireOne__shift_pressed:
                if track.can_be_armed:
                    track.arm = not track.arm
            else:
                track.mute = not track.mute