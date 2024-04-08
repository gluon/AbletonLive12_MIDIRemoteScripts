# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/OpenLabs/SpecialTransportComponent.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 4549 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import Live
import _Framework.ButtonElement as ButtonElement
import _Framework.EncoderElement as EncoderElement
from _Framework.InputControlElement import *
import _Framework.TransportComponent as TransportComponent

class SpecialTransportComponent(TransportComponent):

    def __init__(self):
        TransportComponent.__init__(self)
        self._undo_button = None
        self._redo_button = None
        self._bts_button = None

    def disconnect(self):
        TransportComponent.disconnect(self)
        if self._undo_button != None:
            self._undo_button.remove_value_listener(self._undo_value)
            self._undo_button = None
        if self._redo_button != None:
            self._redo_button.remove_value_listener(self._redo_value)
            self._redo_button = None
        if self._bts_button != None:
            self._bts_button.remove_value_listener(self._bts_value)
            self._bts_button = None

    def set_undo_button(self, undo_button):
        if undo_button != self._undo_button:
            if self._undo_button != None:
                self._undo_button.remove_value_listener(self._undo_value)
            self._undo_button = undo_button
            if self._undo_button != None:
                self._undo_button.add_value_listener(self._undo_value)
            self.update()

    def set_redo_button(self, redo_button):
        if redo_button != self._redo_button:
            if self._redo_button != None:
                self._redo_button.remove_value_listener(self._redo_value)
            self._redo_button = redo_button
            if self._redo_button != None:
                self._redo_button.add_value_listener(self._redo_value)
            self.update()

    def set_bts_button(self, bts_button):
        if bts_button != self._bts_button:
            if self._bts_button != None:
                self._bts_button.remove_value_listener(self._bts_value)
            self._bts_button = bts_button
            if self._bts_button != None:
                self._bts_button.add_value_listener(self._bts_value)
            self.update()

    def _undo_value(self, value):
        if self.is_enabled():
            if not (value != 0 or self._undo_button.is_momentary()):
                if self.song().can_undo:
                    self.song().undo()

    def _redo_value(self, value):
        if self.is_enabled():
            if not (value != 0 or self._redo_button.is_momentary()):
                if self.song().can_redo:
                    self.song().redo()

    def _bts_value(self, value):
        if self.is_enabled():
            self.song().current_song_time = value != 0 or self._bts_button.is_momentary() or 0.0
