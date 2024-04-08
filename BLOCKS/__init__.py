# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/__init__.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 717 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import capabilities as caps
from .blocks import Blocks

def get_capabilities():
    return {(caps.CONTROLLER_ID_KEY): (caps.controller_id(vendor_id=10996,
                                 product_ids=[
                                2304],
                                 model_name=[
                                "Lightpad BLOCK", "BLOCKS"])), 
     
     (caps.PORTS_KEY): [
                        caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]),
                        caps.outport(props=[caps.NOTES_CC, caps.SCRIPT])], 
     
     (caps.TYPE_KEY): "blocks"}


def create_instance(c_instance):
    return Blocks(c_instance=c_instance)
