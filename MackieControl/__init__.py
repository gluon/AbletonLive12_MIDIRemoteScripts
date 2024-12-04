# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl\__init__.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from .MackieControl import MackieControl


def create_instance(c_instance):
    return MackieControl(c_instance)


from _Framework.Capabilities import *


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2675, product_ids=[6],
                                             model_name='MCU Pro USB v3.1'),
            PORTS_KEY: [inport(props=[SCRIPT, REMOTE]), inport(props=[]),
                        inport(props=[]), inport(props=[]),
                        outport(props=[SCRIPT, REMOTE]), outport(props=[]),
                        outport(props=[]), outport(props=[])]}
