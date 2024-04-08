# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/mappings.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3112 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.mode import select_mode_for_main_view
from .midi import PAD_TRANSLATION_CHANNEL

def translate_pad_banks(cs):

    def inner():
        for pad in cs.elements.pad_bank_a_raw + cs.elements.pad_bank_b_raw:
            pad.set_channel(PAD_TRANSLATION_CHANNEL)

    return inner


def realign_encoder_values(cs):

    def inner():
        for encoder in cs.elements.encoders_raw:
            encoder.realign_value()

    return inner


def create_mappings(cs):
    return {'View_Based_Recording':dict(record_button="record_button"), 
     'Transport':dict(loop_button="loop_button",
       play_button="play_button",
       stop_button="stop_button",
       tap_tempo_button="tap_tempo_button"), 
     'Mixer':dict(target_track_arm_button="shifted_display_encoder_button",
       target_track_pan_control="pan_fader",
       target_track_send_a_control="send_a_fader",
       target_track_send_b_control="send_b_fader",
       target_track_volume_control="volume_fader"), 
     'View_Control':dict(track_encoder="shifted_display_encoder"), 
     'Display_Modes':dict(session=(dict(modes=[
      dict(component="View_Control", scene_encoder="display_encoder"),
      dict(component="Session",
        scene_0_launch_button="display_encoder_button")],
       selector=(select_mode_for_main_view("Session")))),
       arrangement=(dict(modes=[
      dict(component="Transport",
        arrangement_position_encoder="display_encoder",
        play_toggle_button="display_encoder_button")],
       selector=(select_mode_for_main_view("Arranger"))))), 
     'Main_Modes':dict(mode_selection_control="firmware_element",
       user=(translate_pad_banks(cs)),
       main=(dict(modes=[
      realign_encoder_values(cs),
      dict(component="Session", clip_launch_buttons="pad_bank_a"),
      dict(component="Drum_Group", matrix="pad_bank_b"),
      dict(component="Device", parameter_controls="encoders")])))}
