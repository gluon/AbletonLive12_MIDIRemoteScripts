# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/loop_selector.py
# Compiled at: 2024-03-11 15:53:16
# Size of source mod 2**32: 8035 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, listens
from ...live import action, get_bar_length, liveobj_changed, liveobj_valid
from .. import Component
from ..controls import ButtonControl, control_matrix
from ..display import Renderable
from ..skin import LiveObjSkinEntry

def quantize_page_time(page_time, bar_length):
    return int(page_time / bar_length) * bar_length


class LoopSelectorComponent(Component, Renderable):
    next_page_button = ButtonControl(color="LoopSelector.Navigation",
      pressed_color="LoopSelector.NavigationPressed")
    prev_page_button = ButtonControl(color="LoopSelector.Navigation",
      pressed_color="LoopSelector.NavigationPressed")
    delete_button = ButtonControl(None)
    matrix = control_matrix(ButtonControl)

    @depends(target_track=None, sequencer_clip=None)
    def __init__(self, name='Loop_Selector', target_track=None, sequencer_clip=None, paginator=None, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._pressed_matrix_indices = []
        self._target_track = target_track
        self._LoopSelectorComponent__on_target_track_color_changed.subject = target_track
        self._clip = None
        self._last_bar_length = sequencer_clip.bar_length
        self._sequencer_clip = sequencer_clip
        self._LoopSelectorComponent__on_sequencer_clip_changed.subject = sequencer_clip
        self.register_slot(sequencer_clip, self._rectify_page_time, "bar_length")
        self.register_slot(sequencer_clip, self._update_matrix, "length")
        self._paginator = paginator
        self._last_page_length = paginator.page_length
        self.register_slot(paginator, self._rectify_page_time, "page_length")
        self.register_slot(paginator, self.update, "page_time")
        self.register_slot(self.song, self._update_matrix, "session_record")
        self.register_slot(self.song, self._update_matrix, "is_playing")
        self.set_clip(self._sequencer_clip.clip)

    @property
    def bar_length(self):
        return get_bar_length(clip=(self._clip))

    def set_matrix(self, matrix):
        self.matrix.set_control_element(matrix)
        self._update_matrix()

    def set_clip(self, clip):
        if liveobj_changed(clip, self._clip):
            self._LoopSelectorComponent__on_playing_position_changed.subject = clip
            self._LoopSelectorComponent__on_playing_status_changed.subject = clip
            self._clip = clip
            if clip:
                if self._paginator.can_change_page:
                    self._paginator.page_time = clip.loop_start
            self.update()

    @matrix.pressed
    def matrix(self, button):
        bar_length = self.bar_length
        if self.delete_button.is_pressed:
            if action.delete_notes_in_range(self._clip, button.index * bar_length, bar_length):
                self.notify(self.notifications.Notes.delete)
            else:
                self.notify(self.notifications.Notes.error_no_notes_to_delete)
        else:
            self._pressed_matrix_indices.append(button.index)
            if len(self._pressed_matrix_indices) > 1:
                action.set_loop_position(self._clip, min(self._pressed_matrix_indices) * bar_length, max(self._pressed_matrix_indices) * bar_length + bar_length)
            self._paginator.page_time = self._pressed_matrix_indices[0] * bar_length

    @matrix.released
    def matrix(self, button):
        if button.index in self._pressed_matrix_indices:
            self._pressed_matrix_indices.remove(button.index)

    @matrix.double_clicked
    def matrix(self, button):
        start = button.index * self.bar_length
        action.set_loop_position(self._clip, start, start + self.bar_length)

    @next_page_button.pressed
    def next_page_button(self, _):
        self._increment_page_time(1)

    @prev_page_button.pressed
    def prev_page_button(self, _):
        self._increment_page_time(-1)

    def _increment_page_time(self, delta):
        self._paginator.page_time = max(0.0, self._paginator.page_length * delta + self._paginator.page_time)

    def _rectify_page_time(self):
        if self._paginator.page_length > self._last_page_length or self.bar_length != self._last_bar_length:
            self._paginator.page_time = quantize_page_time(self._paginator.page_time, self.bar_length)
        self._last_page_length = self._paginator.page_length
        self._last_bar_length = self.bar_length
        self.update()

    def _has_clip(self):
        return liveobj_valid(self._clip)

    def update(self):
        super().update()
        self._update_matrix()
        self._update_page_buttons()

    def _update_matrixParse error at or near `LOAD_FAST' instruction at offset 150

    def _update_matrix_button(self, button, selected, playing, inside_loop):
        color = "OutsideLoop"
        if playing:
            color = "PlayheadRecord" if self.song.session_record else "Playhead"
        else:
            if inside_loop:
                color = "InsideLoopSelected" if selected else "InsideLoop"
            else:
                if selected:
                    color = "OutsideLoopSelected"
        button.color = LiveObjSkinEntry("LoopSelector.{}".format(color), self._target_track.target_track)

    def _update_page_buttons(self):
        has_clip = self._has_clip()
        self.prev_page_button.enabled = has_clip and self._paginator.page_time > 0.0
        self.next_page_button.enabled = has_clip

    @listens("clip")
    def __on_sequencer_clip_changed(self):
        self.set_clip(self._sequencer_clip.clip)

    @listens("playing_position")
    def __on_playing_position_changed(self):
        self._update_matrix()

    @listens("playing_status")
    def __on_playing_status_changed(self):
        self._update_matrix()

    @listens("target_track.color")
    def __on_target_track_color_changed(self):
        self._update_matrix()