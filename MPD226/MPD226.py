# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MPD226/MPD226.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1985 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from itertools import cycle
import _Framework.ButtonMatrixElement as ButtonMatrixElement
from _MPDMkIIBase.ControlElementUtils import make_button, make_encoder, make_slider
import _MPDMkIIBase.MPDMkIIBase as MPDMkIIBase
PAD_CHANNEL = 1
PAD_IDS = [
 [
  81, 83, 84, 86], [74, 76, 77, 79], [67, 69, 71, 72], [60, 62, 64, 65]]

class MPD226(MPDMkIIBase):

    def __init__(self, *a, **k):
        (super(MPD226, self).__init__)(PAD_IDS, PAD_CHANNEL, *a, **k)
        with self.component_guard():
            self._create_device()
            self._create_transport()
            self._create_mixer()

    def _create_controls(self):
        super(MPD226, self)._create_controls()
        self._encoders = ButtonMatrixElement(rows=[
         [make_encoder(identifier, 0 if index < 4 else 1, "Encoder_%d" % index) for index, identifier in zip(range(8), cycle(range(22, 26)))]])
        self._sliders = ButtonMatrixElement(rows=[
         [make_slider(identifier, 0 if index < 4 else 1, "Slider_%d" % index) for index, identifier in zip(range(8), cycle(range(12, 16)))]])
        self._control_buttons = ButtonMatrixElement(rows=[
         [make_button(identifier, 0 if index < 4 else 1, "Control_Button_%d" % index) for index, identifier in zip(range(8), cycle(range(32, 36)))]])
        self._play_button = make_button(118, 0, "Play_Button")
        self._stop_button = make_button(117, 0, "Stop_Button")
        self._record_button = make_button(119, 0, "Record_Button")
