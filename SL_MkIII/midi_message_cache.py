# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/midi_message_cache.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 725 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .sysex import NUM_SET_PROPERTY_HEADER_BYTES

class MidiMessageCache:

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._messages = []

    def __call__(self, message):
        self._messages = list(filter((lambda m: m[None[:NUM_SET_PROPERTY_HEADER_BYTES]] != message[None[:NUM_SET_PROPERTY_HEADER_BYTES]]), self._messages))
        self._messages.append(message)

    @property
    def messages(self):
        return self._messages

    def clear(self):
        self._messages = []
