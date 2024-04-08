# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/parameter_provider.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1758 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, NamedTuple, liveobj_valid
DISCRETE_PARAMETERS_DICT = {"GlueCompressor": ('Ratio', 'Attack', 'Release', 'Peak Clip In')}

def is_parameter_quantized(parameter, parent_device):
    is_quantized = False
    if liveobj_valid(parameter):
        device_class = getattr(parent_device, "class_name", None)
        is_quantized = parameter.is_quantized or device_class in DISCRETE_PARAMETERS_DICT and parameter.name in DISCRETE_PARAMETERS_DICT[device_class]
    return is_quantized


class ParameterInfo(NamedTuple):
    parameter = None
    default_encoder_sensitivity = None
    fine_grain_encoder_sensitivity = None

    def __init__(self, name=None, *a, **k):
        (super(ParameterInfo, self).__init__)(a, _overridden_name=name, **k)

    @property
    def name(self):
        actual_name = self.parameter.name if liveobj_valid(self.parameter) else ""
        return self._overridden_name or actual_name

    def __eq__(self, other_info):
        if not isinstance(other_info, ParameterInfo):
            return NotImplemented
        return super(ParameterInfo, self).__eq__(other_info) and self.name == other_info.name

    def __hash__(self):
        return hash((
         self._overridden_name,
         self.parameter,
         self.default_encoder_sensitivity,
         self.fine_grain_encoder_sensitivity))


class ParameterProvider(EventObject):
    __events__ = ('parameters', )

    @property
    def parameters(self):
        return []
