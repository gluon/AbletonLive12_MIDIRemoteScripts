# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/__init__.py
# Compiled at: 2024-03-11 15:53:42
# Size of source mod 2**32: 718 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .RolandMX1 import RolandMX1

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1410,
                          product_ids=[419],
                          model_name=["MX-1"])), 
     
     PORTS_KEY: [
                 inport(props=[]),
                 inport(props=[SCRIPT]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return RolandMX1(c_instance=c_instance)
