# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/mode/selector.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 3526 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any, NamedTuple, Optional
import Live
from . import pop_last_mode

def select_mode_for_main_view(main_view_name, can_select_now=True):
    return select_mode_on_event_change(EventDescription(subject=(Live.Application.get_application().view),
      event_name="focused_document_view",
      event_state=main_view_name),
      can_select_now=can_select_now)


def select_mode_on_event_change(event_description, can_select_now=False):
    subject = _get_subject(event_description.subject)
    event_name = event_description.event_name
    event_state = event_description.event_state

    def inner(modes_component, mode_name):

        def on_event_changed(*_):
            if event_state is None or getattr(subject, event_name) == event_state:
                modes_component.selected_mode = mode_name

        modes_component.register_slot(subject, on_event_changed, event_name)
        if can_select_now:
            if event_state is not None:
                on_event_changed()

    return inner


def toggle_mode_on_property_change(event_description, return_to_default=False, can_select_now=False):
    subject = _get_subject(event_description.subject)
    event_name = event_description.event_name

    def inner(modes_component, mode_name):

        def on_property_changed(state=None):
            if bool(state or getattr(subject, event_name)):
                modes_component.push_mode(mode_name)
            else:
                if return_to_default and modes_component.selected_mode == mode_name:
                    modes_component.push_mode(modes_component.modes[0])
                    modes_component.pop_unselected_modes()
                else:
                    pop_last_mode(modes_component, mode_name)

        modes_component.register_slot(subject, on_property_changed, event_name)
        if can_select_now:
            on_property_changed(getattr(subject, event_name))

    return inner


def _get_subject(subject):
    if callable(subject):
        return subject()
    return subject


class EventDescription(NamedTuple):
    subject: Any
    event_name: str
    event_state = None
    event_state: Optional[Any]
