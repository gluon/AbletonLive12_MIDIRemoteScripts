# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_mini_mk2/mappings.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3585 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import HIGH_PRIORITY
from ableton.v3.control_surface.mode import ImmediateBehaviour, MomentaryBehaviour, make_reenter_behaviour

def create_mappings(control_surface):
    mappings = {}
    mappings["Mixer"] = dict(master_track_volume_control="master_fader")
    mappings["Session"] = dict(clip_slot_select_button="shift_button")
    mappings["Track_Button_Modes"] = dict(clip_stop=dict(component="Session", stop_track_clip_buttons="track_buttons"),
      solo=dict(component="Mixer", solo_buttons="track_buttons"),
      mute=dict(component="Mixer", mute_buttons="track_buttons"),
      arm=dict(component="Mixer", arm_buttons="track_buttons"),
      track_select=dict(component="Mixer", track_select_buttons="track_buttons"))
    mappings["Fader_Modes"] = dict(volume=dict(component="Mixer", volume_controls="faders"),
      pan=dict(component="Mixer", pan_controls="faders"),
      send=dict(component="Mixer",
      send_controls="faders",
      behaviour=make_reenter_behaviour(ImmediateBehaviour,
      on_reenter=(control_surface.component_map["Mixer"].cycle_send_index))),
      device=dict(component="Device", parameter_controls="faders"))
    mappings["Pad_Modes"] = dict(mode_selection_control="pad_mode_control",
      session=dict(component="Session", clip_launch_buttons="clip_launch_buttons"),
      note=None,
      drum=dict(component="Drum_Group", matrix="drum_pads"),
      note_edit=None)
    mappings["Main_Modes"] = dict(shift_button="shift_button",
      default=dict(component="Session", scene_launch_buttons="scene_launch_buttons"),
      shift=dict(modes=[
     dict(component="Session",
       stop_all_clips_button="scene_launch_buttons_raw[7]"),
     dict(component="Track_Button_Modes",
       clip_stop_button="scene_launch_buttons_raw[0]",
       solo_button="scene_launch_buttons_raw[1]",
       mute_button="scene_launch_buttons_raw[2]",
       arm_button="scene_launch_buttons_raw[3]",
       track_select_button="scene_launch_buttons_raw[4]"),
     dict(component="Fader_Modes",
       volume_button="track_buttons_raw[0]",
       pan_button="track_buttons_raw[1]",
       send_button="track_buttons_raw[2]",
       device_button="track_buttons_raw[3]",
       priority=HIGH_PRIORITY),
     dict(component="Session_Navigation",
       up_button="track_buttons_raw[4]",
       down_button="track_buttons_raw[5]",
       left_button="track_buttons_raw[6]",
       right_button="track_buttons_raw[7]",
       priority=HIGH_PRIORITY)],
      behaviour=(MomentaryBehaviour())))
    return mappings
