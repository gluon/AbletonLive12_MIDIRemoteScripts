# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Faderport_16_XT/__init__.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 777 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from MackieControlXT import MackieControlXT

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=6479,
                          product_ids=[516],
                          model_name=["PreSonus FP16"])), 
     
     PORTS_KEY: [
                 inport(props=[]),
                 inport(props=[SCRIPT, REMOTE]),
                 outport(props=[]),
                 outport(props=[SCRIPT, REMOTE])]}


def create_instance(c_instance):
    return MackieControlXT(c_instance)