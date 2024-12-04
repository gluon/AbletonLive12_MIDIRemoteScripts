# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\__init__.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.control_surface import ControlSurface, \
    ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, \
    PORTS_KEY, SCRIPT, controller_id, inport, outport

try:
    from ableton.v3.control_surface.capabilities import AUTO_LOAD_KEY
except ImportError:
    from ableton.v2.control_surface.capabilities import AUTO_LOAD_KEY
from .active_parameter import ActiveParameterComponent
from .colors import Rgb, Skin
from .display import display_specification
from .elements import Elements
from .mappings import create_mappings
from .midi import CONNECTION_MESSAGE, DISCONNECTION_MESSAGE
from .mixer import MixerComponent
from .mode_buttons import ModeButtonsComponent
from .scene_launch import SceneLaunchComponent


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=7285,
                                             product_ids=[590, 654, 718],
                                             model_name=['KeyLab 49 mk3',
                                                         'KeyLab 61 mk3',
                                                         'KeyLab 88 mk3']),
            PORTS_KEY: [inport(props=[NOTES_CC]),
                        inport(props=[NOTES_CC, SCRIPT]),
                        outport(props=[NOTES_CC]),
                        outport(props=[NOTES_CC, SCRIPT])], AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    return KeyLab_mk3(specification=Specification, c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin, colors=Rgb)
    num_tracks = 4
    num_scenes = 3
    link_session_ring_to_track_selection = True
    link_session_ring_to_scene_selection = True
    include_auto_arming = True
    identity_response_id_bytes = (0, 32, 107, 2, 0, 10)
    create_mappings_function = create_mappings
    hello_messages = (CONNECTION_MESSAGE,)
    goodbye_messages = (DISCONNECTION_MESSAGE,)
    parameter_bank_size = 16
    component_map = {'Active_Parameter': ActiveParameterComponent,
                     'Mixer': MixerComponent,
                     'Mode_Buttons': ModeButtonsComponent,
                     'Scene_Launch': SceneLaunchComponent}
    display_specification = display_specification


class KeyLab_mk3(ControlSurface):

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.set_can_auto_arm(True)
