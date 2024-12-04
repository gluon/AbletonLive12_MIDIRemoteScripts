# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\active_parameter.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.base import find_if, listenable_property
from ableton.v3.control_surface.components import \
    ActiveParameterComponent as ActiveParameterComponentBase
from ableton.v3.live import liveobj_valid


class ActiveParameterComponent(ActiveParameterComponentBase):
    pass

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._is_fader_map = {}

    def set_touch_controls(self, controls):
        self.touch_controls.set_control_element(controls)
        if controls:
            self._is_fader_map = {c: int(c.name.split('_')[-1]) > 8 for c in
                                  controls}

    @listenable_property
    def is_fader(self):
        return self._is_fader_map.get(
            find_if(lambda elem: liveobj_valid(elem.controlled_parameter),
                    (elem for elem in
                     reversed(list(self._pressed_touch_elements.values())))),
            False)

    def notify_parameter(self):
        super().notify_parameter()
        self.notify_is_fader()
