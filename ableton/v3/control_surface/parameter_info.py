# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/parameter_info.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 950 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import ParameterInfo as ParameterInfoBase
from ..live import liveobj_valid

class ParameterInfo(ParameterInfoBase):

    def __init__(self, parameter=None, name=None, *a, **k):
        (super().__init__)(a, parameter=parameter, name=name, **k)
        if liveobj_valid(parameter):
            if name is not None:
                parameter.display_name = name

    @property
    def original_name(self):
        if liveobj_valid(self.parameter):
            return self.parameter.original_name
        return ""
