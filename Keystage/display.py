# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Keystage/display.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1796 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from typing import Optional, Tuple
from ableton.v3.control_surface.display import DisplaySpecification, view
from ableton.v3.live import liveobj_name
Lines = Tuple[(str, str)]

@dataclass
class Content:
    main_lines: Lines
    parameter_displays: Tuple[(Lines, ...)]


def create_root_view() -> view.View[Optional[Content]]:

    @view.View
    def main_view(state) -> Optional[Content]:
        return Content(main_lines=(
         liveobj_name(state.target_track.target_track),
         liveobj_name(state.device.device) or "-"),
          parameter_displays=(tuple(((knob.parameter_name or "-", knob.parameter_value) for knob in state.elements.knobs))))

    return view.CompoundView(view.DisconnectedView(), main_view)


def protocol(elements):

    def display(content):
        if content:
            display_main(content.main_lines)
            display_parameters(content.parameter_displays)

    def display_main(main_lines):
        for element, line in zip(elements.main_display_lines, main_lines):
            element.display_message(line)

    def display_parameters(parameter_displays):
        for display_line_elements, parameter_lines in zip(elements.parameter_display_lines, parameter_displays):
            for element, line in zip(display_line_elements, parameter_lines):
                element.display_message(line)

    return display


display_specification = DisplaySpecification(create_root_view=create_root_view,
  protocol=protocol)
