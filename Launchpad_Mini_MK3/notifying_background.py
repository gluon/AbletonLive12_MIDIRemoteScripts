# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Mini_MK3/notifying_background.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 812 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v2.base import nop
from ableton.v2.control_surface.components import BackgroundComponent
from ableton.v2.control_surface.elements import ButtonMatrixElement

class NotifyingBackgroundComponent(BackgroundComponent):
    __events__ = ('value', )

    def register_slot(self, control, *a):
        listener = nop if isinstance(control, ButtonMatrixElement) else partial(self._NotifyingBackgroundComponent__on_control_value, control)
        return super(BackgroundComponent, self).register_slot(control, listener, "value")

    def __on_control_value(self, control, value):
        self.notify_value(control, value)
