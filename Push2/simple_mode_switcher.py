# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/simple_mode_switcher.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 753 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import const
from pushbase.note_layout_switcher import ModeSwitcherBase

class SimpleModeSwitcher(ModeSwitcherBase):

    def __init__(self, session_modes=None, *a, **k):
        (super(SimpleModeSwitcher, self).__init__)(*a, **k)
        self._session_modes = session_modes
        self._cycle_mode = session_modes.cycle_mode
        self._get_current_alternative_mode = const(session_modes)

    def _unlock_alternative_mode(self, locked_mode):
        super(SimpleModeSwitcher, self)._unlock_alternative_mode(locked_mode)
        self.locked_mode = None
