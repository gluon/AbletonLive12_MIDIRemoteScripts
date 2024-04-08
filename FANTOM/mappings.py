# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FANTOM/mappings.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2221 bytes
from __future__ import absolute_import, print_function, unicode_literals

def create_mappings(_):
    mappings = {}
    mappings["Undo_Redo"] = dict(undo_button="undo_button")
    mappings["Device"] = dict(parameter_controls="device_controls")
    mappings["Drum_Group"] = dict(matrix="drum_pads")
    mappings["Recording"] = dict(arrangement_record_button="record_button",
      arrangement_overdub_button="arrangement_overdub_button",
      session_record_button="session_record_button")
    mappings["Transport"] = dict(play_button="play_button",
      stop_button="stop_button",
      re_enable_automation_button="automation_re-enable_button",
      automation_arm_button="automation_arm_button",
      metronome_button="metronome_button",
      tap_tempo_button="tap_tempo_button",
      capture_midi_button="capture_midi_button",
      tempo_coarse_encoder="tempo_coarse_control",
      tempo_fine_encoder="tempo_fine_control",
      beat_time_display="beat_time_display",
      tempo_display="tempo_display")
    mappings["Mixer"] = dict(volume_controls="volume_controls",
      pan_controls="pan_controls",
      send_a_controls="send_a_controls",
      send_b_controls="send_b_controls",
      track_select_control="track_select_control",
      arm_buttons="arm_buttons",
      solo_buttons="solo_buttons",
      mute_buttons="mute_buttons",
      track_info_display="track_info_display",
      master_track_volume_control="master_volume_control",
      master_track_pan_control="master_pan_control")
    mappings["Session_Navigation"] = dict(up_button="up_button",
      down_button="down_button",
      left_button="left_button",
      right_button="right_button")
    mappings["Session"] = dict(clip_launch_buttons="clip_launch_buttons",
      scene_launch_buttons="scene_launch_buttons",
      stop_track_clip_buttons="stop_track_buttons",
      stop_all_clips_button="stop_all_clips_button",
      track_select_control="track_select_control",
      scene_name_display="scene_name_display")
    return mappings
