# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/LV2_LX2_LC2_LD2/ParamMap.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2995 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range
import Live

class Callable(object):

    def __init__(self, anycallable):
        self.fn = anycallable

    def __call__(self, *a, **k):
        (self.fn)(*a, **k)


class ParamMap(object):
    __module__ = __name__
    __doc__ = "Class to help with device mapping"

    def __init__(self, parent):
        ParamMap.realinit(self, parent)

    def realinit(self, parent):
        self.parent = parent
        self.params_with_listener = []
        self.param_callbacks = []

    def log(self, string):
        self.parent.log(string)

    def logfmt(self, fmt, *args):
        args2 = []
        for i in range(0, len(args)):
            args2 += [args[i].__str__()]

        str = fmt % tuple(args2)
        return self.log(str)

    def param_add_callback(self, script_handle, midi_map_handle, param, min, max, cc, channel):
        callback = lambda: self.on_param_value_changed(param, min, max, cc, channel)
        param.add_value_listener(callback)
        self.params_with_listener += [param]
        self.param_callbacks += [callback]
        ParamMap.forward_cc(script_handle, midi_map_handle, channel, cc)

    def receive_midi_note(self, channel, status, note_no, note_vel):
        pass

    def receive_midi_cc(self, chan, cc_no, cc_value):
        pass

    def forward_cc(script_handle, midi_map_handle, chan, cc):
        Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, chan, cc)

    forward_cc = Callable(forward_cc)

    def forward_note(script_handle, midi_map_handle, chan, note):
        Live.MidiMap.forward_midi_note(script_handle, midi_map_handle, chan, note)

    forward_note = Callable(forward_note)

    def map_with_feedback(midi_map_handle, channel, cc, parameter, mode):
        feedback_rule = Live.MidiMap.CCFeedbackRule()
        feedback_rule.channel = channel
        feedback_rule.cc_value_map = tuple()
        feedback_rule.delay_in_ms = -1.0
        feedback_rule.cc_no = cc
        Live.MidiMap.map_midi_cc_with_feedback_map(midi_map_handle, parameter, channel, cc, mode, feedback_rule, False)
        Live.MidiMap.send_feedback_for_parameter(midi_map_handle, parameter)

    map_with_feedback = Callable(map_with_feedback)

    def on_param_value_changed(self, param, min, max, cc, channel):
        pass

    def remove_mappings(self):
        for i in range(0, len(self.params_with_listener)):
            param = self.params_with_listener[i]
            callback = self.param_callbacks[i]
            try:
                if param.value_has_listener(callback):
                    param.remove_value_listener(callback)
            except:
                continue

        self.params_with_listener = []
        self.param_callbacks = []
