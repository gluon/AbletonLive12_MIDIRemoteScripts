# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/device_util.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1134 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import liveobj_valid

def is_drum_pad(item):
    return liveobj_valid(item) and isinstance(item, Live.DrumPad.DrumPad)


def find_chain_or_track(item):
    if is_drum_pad(item) and item.chains:
        chain = item.chains[0]
    else:
        chain = item
        while liveobj_valid(chain):
            chain = isinstance(chain, (Live.Track.Track, Live.Chain.Chain)) or getattr(chain, "canonical_parent", None)

    return chain


def find_rack(item):
    rack = item
    while liveobj_valid(rack):
        rack = isinstance(rack, Live.RackDevice.RackDevice) or getattr(rack, "canonical_parent", None)

    return rack
