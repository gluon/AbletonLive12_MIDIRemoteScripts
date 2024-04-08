# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/eq3.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 755 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class EqThreeDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(EqThreeDeviceDecorator, self).__init__)(*a, **k)
        self._add_switch_option(name="Slope", pname="Slope", labels=["24dB", "48dB"])
        self._add_on_off_option(name="Low", pname="LowOn")
        self._add_on_off_option(name="Mid", pname="MidOn")
        self._add_on_off_option(name="High", pname="HighOn")
        self.register_disconnectables(self.options)
