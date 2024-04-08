# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/cccontrol.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3699 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, find_if, listens, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name
from .device_options import DeviceOnOffOption, DeviceSwitchOption, DeviceTriggerOption

class CcControlDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(CcControlDeviceDecorator, self).__init__)(*a, **k)
        self._add_non_automatable_enum_parameter(name="Custom Button Target",
          list="custom_bool_target_list",
          index="custom_bool_target")
        self._add_non_automatable_enum_parameter(name="Custom Target 1",
          list="custom_float_target_0_list",
          index="custom_float_target_0")
        self._add_non_automatable_enum_parameter(name="Custom Target 2",
          list="custom_float_target_1_list",
          index="custom_float_target_1")
        self._add_non_automatable_enum_parameter(name="Custom Target 3",
          list="custom_float_target_2_list",
          index="custom_float_target_2")
        self._add_non_automatable_enum_parameter(name="Custom Target 4",
          list="custom_float_target_3_list",
          index="custom_float_target_3")
        self._add_non_automatable_enum_parameter(name="Custom Target 5",
          list="custom_float_target_4_list",
          index="custom_float_target_4")
        self._add_non_automatable_enum_parameter(name="Custom Target 6",
          list="custom_float_target_5_list",
          index="custom_float_target_5")
        self._add_non_automatable_enum_parameter(name="Custom Target 7",
          list="custom_float_target_6_list",
          index="custom_float_target_6")
        self._add_non_automatable_enum_parameter(name="Custom Target 8",
          list="custom_float_target_7_list",
          index="custom_float_target_7")
        self._add_non_automatable_enum_parameter(name="Custom Target 9",
          list="custom_float_target_8_list",
          index="custom_float_target_8")
        self._add_non_automatable_enum_parameter(name="Custom Target 10",
          list="custom_float_target_9_list",
          index="custom_float_target_9")
        self._add_non_automatable_enum_parameter(name="Custom Target 11",
          list="custom_float_target_10_list",
          index="custom_float_target_10")
        self._add_non_automatable_enum_parameter(name="Custom Target 12",
          list="custom_float_target_11_list",
          index="custom_float_target_11")
        self._options = self._create_options()
        self.register_disconnectables(self._options)

    @property
    def options(self):
        return self._options

    def _create_options(self):

        def get_parameter_by_original_name(name):
            return find_if((lambda p: p.original_name == name), self._live_object.parameters)

        def call_resend():
            if liveobj_valid(self._live_object):
                return self._live_object.resend()

        return (
         DeviceTriggerOption(name="Resend", callback=call_resend),
         DeviceOnOffOption(name="Button",
           property_host=(get_parameter_by_original_name("Custom 1"))))
