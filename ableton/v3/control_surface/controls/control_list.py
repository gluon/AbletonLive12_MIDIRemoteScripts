# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/controls/control_list.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3242 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import ControlList as ControlListBase
from ...base import mixin
from . import RadioButtonGroup
_control_list_types = {}

def control_list(control_type, *a, **k):
    factory = _control_list_types.get(control_type, None)
    if not factory:
        factory = mixin(ControlList, control_type)
        _control_list_types[control_type] = factory
    return factory(control_type, *a, **k)


class ControlList(ControlListBase):

    class State(ControlListBase.State):

        def set_control_element_at_index(self, control_element, index):
            if self._control_elements:
                num_elements = len(self._control_elements)
                if num_elements > index:
                    self._control_elements[index] = control_element
                else:
                    self._control_elements.extend([
                     None] * (index - num_elements) + [control_element])
            else:
                self._control_elements = [
                 None] * index + [control_element]
            self._update_controls()


class FixedRadioButtonGroup(RadioButtonGroup):

    class State(RadioButtonGroup.State):

        def __init__(self, *a, **k):
            (super().__init__)(*a, **k)
            self._active_control_count = 0

        @property
        def active_control_count(self):
            return self._active_control_count

        @active_control_count.setter
        def active_control_count(self, control_count):
            self._active_control_count = control_count
            for index, control in enumerate(self._controls):
                control._get_state(self._manager).enabled = index < control_count
