# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/event_signal/core.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 524 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any
from notifications.type_decl import NOTIFICATION_EVENT_ID
from ..state import State
from ..type_decl import Event
from .type_decl import EventSignalFn

def on_notification() -> EventSignalFn[Any]:

    def signal_fn(_: State, event: Event):
        if event.name == NOTIFICATION_EVENT_ID:
            return event.value

    return signal_fn
