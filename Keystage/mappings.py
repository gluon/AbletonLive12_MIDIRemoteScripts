# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Keystage/mappings.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 824 bytes
from __future__ import absolute_import, print_function, unicode_literals

def create_mappings(_):
    mappings = {}
    mappings["Transport"] = dict(play_button="play_button",
      stop_button="stop_button",
      loop_button="loop_button",
      tap_tempo_button="tempo_button",
      metronome_button="metronome_button",
      rewind_button="rewind_button",
      fastforward_button="fastforward_button")
    mappings["View_Based_Recording"] = dict(record_button="record_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button")
    mappings["View_Control"] = dict(prev_track_button="up_button",
      next_track_button="down_button")
    mappings["Device"] = dict(parameter_controls="knobs")
    return mappings
