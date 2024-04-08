# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/LV2_LX2_LC2_LD2/FaderfoxTransportController.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 6803 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import Live
from .consts import *
from .FaderfoxComponent import FaderfoxComponent

class FaderfoxTransportController(FaderfoxComponent):
    __module__ = __name__
    __doc__ = "Class representing the transport section of faderfox controllers"
    __filter_funcs__ = ["update_display", "log"]

    def __init__(self, parent):
        FaderfoxTransportController.realinit(self, parent)

    def realinit(self, parent):
        FaderfoxComponent.realinit(self, parent)

    def receive_midi_cc(self, channel, cc_no, cc_value):
        if channel == CHANNEL_SETUP2:
            if cc_no == SCENE_SCROLL_CC:
                val = 0
                if cc_value >= 64:
                    val = cc_value - 128
                else:
                    val = cc_value
                idx = self.helper.selected_scene_idx() - val
                new_scene_idx = min(len(self.parent.song().scenes) - 1, max(0, idx))
                self.parent.song().view.selected_scene = self.parent.song().scenes[new_scene_idx]

    def receive_midi_noteParse error at or near `LOAD_FAST' instruction at offset 690

    def trigger_track_clip(self, track_idx, clip_idx):
        self.helper.trigger_track_clip(track_idx, clip_idx)

    def stop_track(self, track_idx):
        self.helper.stop_track(track_idx)

    def build_midi_map(self, script_handle, midi_map_handle):

        def forward_note(chan, note):
            Live.MidiMap.forward_midi_note(script_handle, midi_map_handle, chan, note)

        def forward_cc(chan, cc):
            Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, chan, cc)

        forward_cc(CHANNEL_SETUP2, SCENE_SCROLL_CC)
        forward_note(CHANNEL_SETUP2, SCENE_UP_NOTE)
        forward_note(CHANNEL_SETUP2, SCENE_DOWN_NOTE)
        for note in LAUNCH_NOTES:
            forward_note(TRACK_CHANNEL_SETUP2, note)

        for note in STOP_NOTES:
            forward_note(TRACK_CHANNEL_SETUP2, note)

        forward_note(CHANNEL_SETUP2, SCENE_LAUNCH_NOTE)
        forward_note(CHANNEL_SETUP2, SCENE_STOP_NOTE)
        for note in [
         CLIP_SELECT_NOTE, 
         GLOBAL_STOP_NOTE, 
         GLOBAL_PLAY_NOTE, 
         SESSION_ARRANGE_SWITCH_NOTE, 
         CLIP_TRACK_SWITCH_NOTE]:
            forward_note(CHANNEL_SETUP2, note)

        for note in SCENE_LAUNCH_NOTES:
            forward_note(CHANNEL_SETUP2, note)

        for notes in SLOT_LAUNCH_NOTES1:
            for note in notes:
                forward_note(AUX_CHANNEL_SETUP2, note)

        for notes in SLOT_LAUNCH_NOTES2:
            for note in notes[0[:2]]:
                forward_note(AUX_CHANNEL_SETUP2, note)

            for note in notes[2[:None]]:
                forward_note(CHANNEL_SETUP2, note)

    def disconnect(self):
        pass