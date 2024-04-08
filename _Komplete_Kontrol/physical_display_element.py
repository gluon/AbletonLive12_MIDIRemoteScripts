# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/physical_display_element.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 647 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import str
from itertools import chain
from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase

class PhysicalDisplayElement(PhysicalDisplayElementBase):

    def _build_display_message(self, display):
        return chain(*map((lambda x: self._translate_string(str(x).strip())), display._logical_segments))

    def _request_send_message(self):
        self._send_message()
