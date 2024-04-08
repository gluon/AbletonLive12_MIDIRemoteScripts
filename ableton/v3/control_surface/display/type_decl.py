# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/type_decl.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1109 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any, Callable, NamedTuple, TypeVar
from .state import State

class Event(NamedTuple):
    name: str
    origin: Any
    value: Any


INIT_EVENT = Event(name="init", origin=None, value=None)
DISCONNECT_EVENT = Event(name="disconnect", origin=None, value=None)
ContentType = TypeVar("ContentType")
Render = Callable[([State], ContentType)]
