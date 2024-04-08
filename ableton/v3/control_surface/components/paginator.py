# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/paginator.py
# Compiled at: 2024-03-11 10:58:37
# Size of source mod 2**32: 2492 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import EventObject, depends, forward_property, listens
from .. import Component

class Paginator(EventObject):
    __events__ = ('page', 'page_time', 'page_length')
    can_change_page = NotImplemented
    page_length = NotImplemented
    page_time = NotImplemented


class NoteEditorPaginator(Component, Paginator):
    can_change_page = forward_property("_note_editor")("can_change_page")
    page_length = forward_property("_note_editor")("page_length")

    @depends(note_editor=None)
    def __init__(self, note_editor=None, *a, **k):
        (super().__init__)(*a, **k)
        self._note_editor = note_editor
        self._last_page_time = 0.0
        self._NoteEditorPaginator__on_page_length_changed.subject = note_editor
        self._NoteEditorPaginator__on_active_steps_changed.subject = note_editor

    @property
    def page_time(self):
        return self._note_editor.page_time

    @page_time.setter
    def page_time(self, time):
        can_change_page = self.can_change_page
        if can_change_page:
            if time != self._last_page_time:
                self._note_editor.page_time = time
                self._last_page_time = time
                self.notify_page()
                self.notify_page_time()

    def update(self):
        super().update()
        if self.is_enabled():
            self.notify_page_time()
            self.notify_page()
            self.notify_page_length()

    @listens("active_steps")
    def __on_active_steps_changed(self):
        if self.is_enabled():
            self.notify_page()

    @listens("page_length")
    def __on_page_length_changed(self):
        if self.is_enabled():
            self.notify_page()
            self.notify_page_length()
