# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/clip_actions.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2029 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface.components import ClipActionsComponent as ClipActionsComponentBase
from ableton.v2.control_surface.control import ButtonControl
from .control import SendReceiveValueControl
RecordingQ = Live.Song.RecordingQuantization

def is_valid_quantize_value(value):
    return RecordingQ.rec_q_quarter <= value <= RecordingQ.rec_q_thirtysecond


class ClipActionsComponent(ClipActionsComponentBase):
    quantization_value_control = SendReceiveValueControl()
    quantize_button = ButtonControl()
    quantize_color_control = ButtonControl()

    def __init__(self, *a, **k):
        (super(ClipActionsComponent, self).__init__)(*a, **k)
        self._quantization_value = RecordingQ.rec_q_sixtenth
        self.quantization_value_control.value = self._quantization_value - 1
        self.duplicate_button.pressed_color = "Action.On"
        self.delete_button.pressed_color = "Action.On"

    @quantization_value_control.value
    def quantizaton_value_control(self, value, _):
        self._quantization_value = value + 1

    @quantize_button.pressed
    def quantize_button(self, _):
        quantize_to = self._quantization_value
        if self._can_perform_clip_action():
            if is_valid_quantize_value(quantize_to):
                self.clip_slot.clip.quantize(quantize_to, 1.0)
        self._update_quantize_color_control()

    @quantize_button.released
    def quantize_button(self, _):
        self._update_quantize_color_control()

    def _update_action_buttons(self):
        super(ClipActionsComponent, self)._update_action_buttons()
        self._update_quantize_color_control()

    def _update_quantize_color_control(self):
        self.quantize_color_control.color = "Action.QuantizeOn" if (self.quantize_button.is_pressed and self._can_perform_clip_action()) else "Action.QuantizeOff"
