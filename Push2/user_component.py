# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/user_component.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1789 bytes
from __future__ import absolute_import, print_function, unicode_literals
from contextlib import contextmanager
from ableton.v2.control_surface.mode import ModeButtonBehaviour
from pushbase.user_component import UserComponentBase
from . import sysex

class UserButtonBehavior(ModeButtonBehaviour):

    def __init__(self, user_component=None, *a, **k):
        (super(UserButtonBehavior, self).__init__)(*a, **k)
        self._previous_mode = None
        self._user_component = user_component

    def press_immediate(self, component, mode):
        if component.selected_mode != "user" and self._user_component.mode == sysex.LIVE_MODE:
            self._previous_mode = component.selected_mode
            component.selected_mode = "user"
        else:
            self._leave_user_mode(component)

    def release_delayed(self, component, mode):
        self._leave_user_mode(component)

    def _leave_user_mode(self, component):
        if component.selected_mode == "user":
            if self._user_component.mode == sysex.USER_MODE:
                component.selected_mode = self._previous_mode
                self._previous_mode = None


class UserComponent(UserComponentBase):

    @contextmanager
    def _deferring_sysex(self):
        self.defer_sysex_sending = True
        yield
        self.defer_sysex_sending = False

    def _do_set_mode(self, mode):
        if mode == sysex.USER_MODE:
            with self._deferring_sysex():
                super(UserComponent, self)._do_set_mode(mode)
        else:
            super(UserComponent, self)._do_set_mode(mode)
