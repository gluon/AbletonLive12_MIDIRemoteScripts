# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/control_surface_specification.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 7946 bytes
from __future__ import absolute_import, print_function, unicode_literals
from types import SimpleNamespace
from . import DEFAULT_BANK_SIZE, BasicColors, DeviceProvider, midi
from .components import AutoArmComponent, BasicRecordingMethod, SessionRingComponent, TargetTrackComponent
from .consts import LOW_PRIORITY
from .default_bank_definitions import BANK_DEFINITIONS
from .default_skin import default_skin
from .display import DisplaySpecification
from .parameter_mapping_sensitivities import DEFAULT_CONTINUOUS_PARAMETER_SENSITIVITY, DEFAULT_QUANTIZED_PARAMETER_SENSITIVITY

class ControlSurfaceSpecification(SimpleNamespace):
    elements_type = None
    control_surface_skin = default_skin
    display_specification = DisplaySpecification()
    num_tracks = 8
    num_scenes = 1
    include_returns = False
    include_master = False
    right_align_non_player_tracks = False
    snap_track_offset = False
    include_auto_arming = False
    link_session_ring_to_track_selection = False
    link_session_ring_to_scene_selection = False
    session_ring_component_type = SessionRingComponent
    target_track_component_type = TargetTrackComponent
    auto_arm_component_type = AutoArmComponent
    device_provider_type = DeviceProvider
    recording_method_type = BasicRecordingMethod
    feedback_channels = None
    playing_feedback_velocity = BasicColors.ON.midi_value
    recording_feedback_velocity = BasicColors.ON.midi_value
    background_priority = LOW_PRIORITY
    identity_response_id_bytes = None
    custom_identity_response = None
    identity_request = midi.SYSEX_IDENTITY_REQUEST_MESSAGE
    identity_request_delay = 0.0
    hello_messages = None
    goodbye_messages = None
    send_goodbye_messages_last = True
    create_mappings_function = lambda *x: {}
    component_map = {}
    parameter_bank_definitions = BANK_DEFINITIONS
    parameter_bank_size = DEFAULT_BANK_SIZE
    continuous_parameter_sensitivity = DEFAULT_CONTINUOUS_PARAMETER_SENSITIVITY
    quantized_parameter_sensitivity = DEFAULT_QUANTIZED_PARAMETER_SENSITIVITY
