# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MxDCore/NotesAPIUtils.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1246 bytes
from __future__ import absolute_import, print_function, unicode_literals
MIDI_NOTE_ATTRS = ('note_id', 'pitch', 'start_time', 'duration', 'velocity', 'mute',
                   'probability', 'velocity_deviation', 'release_velocity')
REQUIRED_MIDI_NOTE_ATTRS = ('pitch', 'start_time', 'duration')
VALID_DUPLICATE_NOTES_BY_ID_PARAMETERS = ('note_ids', 'destination_time', 'transposition_amount')

def midi_note_to_dict(note, properties_to_return=None):

    def get_note_attr(attr_name):
        prop = getattr(note, attr_name)
        if attr_name == "mute":
            return int(prop)
        return prop

    note_dict = {}
    for attr in MIDI_NOTE_ATTRS:
        if properties_to_return is None or attr in properties_to_return:
            note_dict[attr] = get_note_attr(attr)

    return note_dict


def midi_notes_to_notes_dict(notes):
    return {"notes": [midi_note_to_dict(note) for note in notes]}


def verify_note_specification_requirements(note_specification):
    missing_keys = set(REQUIRED_MIDI_NOTE_ATTRS) - set(note_specification.keys())
    if len(missing_keys) > 0:
        raise RuntimeError("Missing required keys: ", ", ".join(missing_keys))
