# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/mappings.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 2046 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.mode import select_mode_for_main_view

def create_mappings(_):
    mappings = {}
    mappings["Focus_Follow"] = dict(focus_follow_control="focus_follow_element")
    mappings["Transport"] = dict(play_pause_button="play_button",
      play_button="restart_button",
      stop_button="stop_button",
      loop_button="loop_button",
      metronome_button="metro_button",
      tap_tempo_button="tempo_button",
      automation_arm_button="auto_button",
      loop_start_encoder="loop_start_encoder")
    mappings["Launch_And_Stop"] = dict(launch_button="clip_launch_button",
      stop_button="track_stop_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button", redo_button="redo_button")
    mappings["Clip_Actions"] = dict(quantize_button="quantize_button")
    mappings["Session_Navigation"] = dict(track_bank_encoder="track_bank_encoder")
    mappings["View_Control"] = dict(scene_encoder="scene_encoder",
      track_encoder="track_encoder")
    mappings["Mixer"] = dict(enable=False,
      volume_controls="volume_encoders",
      pan_controls="pan_encoders",
      mute_buttons="track_mute_element",
      solo_buttons="track_solo_element",
      target_track_volume_control="track_volume_encoder",
      target_track_pan_control="track_pan_encoder")
    mappings["Recording_Modes"] = dict(session=dict(component="Recording",
      session_record_button="record_button",
      arrangement_record_button="count_in_button",
      selector=(select_mode_for_main_view("Session"))),
      arrange=dict(component="Recording",
      arrangement_record_button="record_button",
      session_record_button="count_in_button",
      selector=(select_mode_for_main_view("Arranger"))))
    return mappings
