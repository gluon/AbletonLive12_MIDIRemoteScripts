# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/with_priority.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 622 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import DEFAULT_PRIORITY
from ableton.v2.control_surface.elements import WrapperElement

class WithPriority(WrapperElement):

    def __init__(self, wrapped_priority=DEFAULT_PRIORITY, *a, **k):
        (super(WithPriority, self).__init__)(*a, **k)
        self.wrapped_priority = wrapped_priority
        self.register_control_element(self.wrapped_control)

    def get_control_element_priority(self, element, priority):
        return self.wrapped_priority
