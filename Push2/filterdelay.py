# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/filterdelay.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1389 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class FilterDelayDeviceDecorator(LiveObjectDecorator, EventObject):

    class ChanSelect(IntEnum):
        l = 0
        lr = 1
        r = 2
        dry = 3

    def __init__(self, *a, **k):
        (super(FilterDelayDeviceDecorator, self).__init__)(*a, **k)
        self._add_enum_parameter(name="Chan Select",
          values=[
         "L", "L+R", "R", "Dry"],
          default_value=(self.ChanSelect.l))
        self._add_on_off_option(name="L Sync", pname="1 Delay Mode")
        self._add_on_off_option(name="L+R Sync", pname="2 Delay Mode")
        self._add_on_off_option(name="R Sync", pname="3 Delay Mode")
        self._add_on_off_option(name="L Channel", pname="1 Input On")
        self._add_on_off_option(name="L+R Channel", pname="2 Input On")
        self._add_on_off_option(name="R Channel", pname="3 Input On")
        self._add_on_off_option(name="L Filter", pname="1 Filter On")
        self._add_on_off_option(name="L+R Filter", pname="2 Filter On")
        self._add_on_off_option(name="R Filter", pname="3 Filter On")
        self.register_disconnectables(self.options)
