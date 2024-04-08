# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOMSQ/display.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2407 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from typing import Optional, Tuple
from ableton.v3.control_surface.display import DefaultNotifications, DisplaySpecification, view
from ableton.v3.live import liveobj_name
BUTTON_LABELS_MAP = {
 'song': ('Solo', 'Mute', 'Arm', 'Clip', 'Scene', 'Stop'), 
 'instrument': ('-', '-', '-', '-', '-', '-'), 
 'editor': ('Lock', '< Device', 'Device >', 'On/Off', '< Bank', 'Bank >'), 
 'user': ('User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6')}

@dataclass
class Content:
    track_name = None
    track_name: Optional[str]
    device_or_bank_name = None
    device_or_bank_name: Optional[str]
    button_labels = (None, None, None, None, None, None)
    button_labels: Optional[Tuple[(str, str, str, str, str, str)]]


class Notifications(DefaultNotifications):

    class Device(DefaultNotifications.Device):
        bank = DefaultNotifications.DefaultText()


def create_root_view() -> view.View[Optional[Content]]:

    @view.View
    def main_view(state) -> Optional[Content]:
        return Content(track_name=(liveobj_name(state.target_track.target_track)),
          device_or_bank_name=(liveobj_name(state.device.device) or "-"),
          button_labels=(BUTTON_LABELS_MAP[state.main_modes.selected_mode]))

    def notification_content(state, text):
        main_content = main_view(state)
        main_content.device_or_bank_name = text
        return main_content

    return view.CompoundView(view.NotificationView(notification_content), main_view)


def protocol(elements):

    def display(content):
        if content:
            if content.track_name:
                elements.track_name_display.display_message(content.track_name)
            if content.device_or_bank_name:
                elements.device_name_display.display_message(content.device_or_bank_name)
            display_button_labels(content)

    def display_button_labels(content):
        if content.button_labels:
            for i, text in enumerate(content.button_labels):
                getattr(elements, "button_label_display_{}".format(i)).display_message(text)

    return display


display_specification = DisplaySpecification(create_root_view=create_root_view,
  protocol=protocol,
  notifications=Notifications)
