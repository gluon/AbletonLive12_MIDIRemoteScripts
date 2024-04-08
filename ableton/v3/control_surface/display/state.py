# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/state.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 3207 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from pprint import pformat
from typing import Callable, Optional
from weakref import ref
import Live

@dataclass
class StateFilters:
    key_filter = lambda k: not k.startswith("_")
    key_filter: Callable
    value_filter = lambda v: v is not None and v != ""
    value_filter: Callable


class State:
    repr_filters = StateFilters()

    def __init__(self):
        super().__init__()
        self._timers = {}

    def __repr__(self):
        return pformat((self.get_repr_data()), indent=4)

    def set_delayed(self, attr_name: str, value, delay_time: Optional[float]):
        if delay_time is None:
            setattr(self, attr_name, value)
        else:
            _self = ref(self)

            def do_setattr():
                if _self():
                    setattr(_self(), attr_name, value)
                    del getattr(_self(), "_timers")[attr_name]

            self._timers[attr_name] = Live.Base.Timer(callback=do_setattr,
              interval=(int(delay_time * 1000)),
              start=True)

    def get_repr_data(self):
        return State.as_dict(self, self.repr_filters)

    @staticmethod
    def as_dict(instance, state_filters=StateFilters(value_filter=(lambda _: True))):
        if isinstance(instance, dict):
            return instance
        dct = dict(vars(instance))
        keys_to_remove = set()
        for key, value in dct.items():
            if not state_filters.key_filter(key):
                keys_to_remove.add(key)
            else:
                if isinstance(value, State):
                    dct[key] = State.as_dict(value, state_filters)

        for key in keys_to_remove:
            del dct[key]

        return dct

    def trigger_timers(self, from_test=False):
        for timer in list(self._timers.values()):
            timer.trigger()
