# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/drum_group.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 726 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import DrumGroupComponent as DrumGroupComponentBase
from .util import skin_scroll_buttons

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, *a, **k):
        (super(DrumGroupComponent, self).__init__)(*a, **k)
        skin_scroll_buttons(self._position_scroll, "DrumGroup.Navigation", "DrumGroup.NavigationPressed")
        skin_scroll_buttons(self._page_scroll, "DrumGroup.Navigation", "DrumGroup.NavigationPressed")

    def set_parent_track(self, track):
        pass
