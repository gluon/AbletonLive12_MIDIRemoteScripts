# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/drum_group_scroll.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2582 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...live import liveobj_valid
from ..display import Renderable
from .page import Pageable, PageComponent
MAX_DRUM_GROUP_SCROLL_POSITION = 28

class DrumGroupScrollComponent(PageComponent, Pageable, Renderable):
    position_count = 32
    page_length = 4
    page_offset = 1

    def __init__(self, name='Drum_Group_Scroll', *a, **k):
        self._drum_group_device = None
        (super().__init__)(a, name=name, scroll_skin_name="DrumGroup.Scroll", **k)

    def set_scroll_encoder(self, encoder):
        self._position_scroll.set_scroll_encoder(encoder)

    def set_drum_group_device(self, drum_group_device):
        self._drum_group_device = drum_group_device
        self.update()

    @property
    def position(self):
        if liveobj_valid(self._drum_group_device):
            return self._drum_group_device.view.drum_pads_scroll_position
        return 0

    @position.setter
    def position(self, index):
        if liveobj_valid(self._drum_group_device):
            self._drum_group_device.view.drum_pads_scroll_position = index

    def can_scroll_page_up(self):
        if not liveobj_valid(self._drum_group_device):
            return False
        return super().can_scroll_page_up()

    def scroll_page_up(self):
        super().scroll_page_up()
        self.notify(self.notifications.DrumGroup.Page.up)

    def scroll_page_down(self):
        super().scroll_page_down()
        self.notify(self.notifications.DrumGroup.Page.down)

    def scroll_up(self):
        super().scroll_up()
        self.notify(self.notifications.DrumGroup.Scroll.up)

    def scroll_down(self):
        super().scroll_down()
        self.notify(self.notifications.DrumGroup.Scroll.down)
