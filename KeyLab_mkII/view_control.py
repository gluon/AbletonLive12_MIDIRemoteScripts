# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/view_control.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1225 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import find_if, listens, liveobj_valid
from ableton.v2.control_surface.control import ButtonControl
from KeyLab_Essential.view_control import ViewControlComponent as ViewControlComponentBase
MAIN_VIEWS = ('Session', 'Arranger')

class ViewControlComponent(ViewControlComponentBase):
    document_view_toggle_button = ButtonControl()

    def __init__(self, *a, **k):
        (super(ViewControlComponent, self).__init__)(*a, **k)
        self._ViewControlComponent__on_focused_document_view_changed.subject = self.application.view
        self._ViewControlComponent__on_focused_document_view_changed()

    @document_view_toggle_button.pressed
    def document_view_toggle_button(self, _):
        is_session_visible = self.application.view.is_view_visible("Session",
          main_window_only=True)
        self.show_view("Arranger" if is_session_visible else "Session")

    @listens("focused_document_view")
    def __on_focused_document_view_changed(self):
        self.document_view_toggle_button.color = "View.{}".format(self.application.view.focused_document_view)
