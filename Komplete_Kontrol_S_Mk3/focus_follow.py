# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/focus_follow.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1789 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live.PluginDevice as PluginDevice
from ableton.v3.control_surface import InstrumentFinderComponent, find_instrument_meeting_requirement
from ableton.v3.control_surface.controls import SendValueControl
from ableton.v3.live import liveobj_valid
PLUGIN_NAME_PREFIXES = ('Komplete Kontrol', 'Kontakt')
KONTAKT_PARAMETER_NAME_PREFIX = "NIKT"

def get_parameter_name_for_instance(instance):
    param_names = instance.get_parameter_names()
    if param_names:
        if instance.name.startswith("Komplete Kontrol"):
            return param_names[0]
        for index in (2048, 4096):
            if index < len(param_names) and param_names[index].startswith(KONTAKT_PARAMETER_NAME_PREFIX):
                return param_names[index]

    return ""


class FocusFollowComponent(InstrumentFinderComponent):
    focus_follow_control = SendValueControl()

    def _update_instruments(self):
        instance = find_instrument_meeting_requirement((lambda d: isinstance(d, PluginDevice) and d.name.startswith(PLUGIN_NAME_PREFIXES)), self._target_track.target_track)
        param_name = ""
        if liveobj_valid(instance):
            param_name = get_parameter_name_for_instance(instance)
        self.focus_follow_control.value = tuple((ord(n) for n in param_name))
