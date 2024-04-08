# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_mini_mk2/__init__.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 2309 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listens
from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, HIDDEN, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, controller_id, inport, outport
from ableton.v3.control_surface.components import DEFAULT_DRUM_TRANSLATION_CHANNEL
from .colors import Rgb, Skin
from .elements import PAD_MODE_HEADER, SYSEX_END, Elements
from .mappings import create_mappings

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[79],
                          model_name=["APC mini mk2"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[NOTES_CC]),
                 outport(props=[NOTES_CC, SCRIPT, SYNC, HIDDEN]),
                 outport(props=[NOTES_CC])]}


def create_instance(c_instance):
    return APC_mini_mk2(c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin, colors=Rgb)
    num_tracks = 8
    num_scenes = 8
    include_returns = True
    feedback_channels = [DEFAULT_DRUM_TRANSLATION_CHANNEL]
    playing_feedback_velocity = Rgb.GREEN.midi_value
    recording_feedback_velocity = Rgb.RED.midi_value
    identity_response_id_bytes = (71, 79, 0, 25)
    goodbye_messages = (PAD_MODE_HEADER + (0, SYSEX_END),)
    create_mappings_function = create_mappings


class APC_mini_mk2(ControlSurface):

    def __init__(self, *a, **k):
        (super().__init__)(Specification, *a, **k)

    def setup(self):
        super().setup()
        self._APC_mini_mk2__on_pad_mode_changed.subject = self.component_map["Pad_Modes"]

    @staticmethod
    def _should_include_element_in_background(element):
        return "Drum_Pad" not in element.name

    @listens("selected_mode")
    def __on_pad_mode_changed(self, selected_mode):
        is_drum_mode = selected_mode == "drum"
        self.set_can_update_controlled_track(is_drum_mode)
        if is_drum_mode:
            self.refresh_state()
