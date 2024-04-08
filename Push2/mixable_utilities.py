# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/mixable_utilities.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 981 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import old_hasattr
from ableton.v2.control_surface import find_instrument_meeting_requirement

def is_chain(track_or_chain):
    return isinstance(getattr(track_or_chain, "proxied_object", track_or_chain), Live.Chain.Chain)


def is_midi_track(track):
    return getattr(track, "has_midi_input", False) and not is_chain(track)


def is_audio_track(track):
    return getattr(track, "has_audio_input", False) and not is_chain(track)


def can_play_clips(mixable):
    return old_hasattr(mixable, "fired_slot_index")


def find_drum_rack_instrument(track):
    return find_instrument_meeting_requirement((lambda i: i.can_have_drum_pads), track)


def find_simpler(track_or_chain):
    return find_instrument_meeting_requirement((lambda i: old_hasattr(i, "playback_mode")), track_or_chain)
