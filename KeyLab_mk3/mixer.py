# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\mixer.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.base import find_if, listenable_property, nop
from ableton.v3.control_surface.components import \
    MixerComponent as MixerComponentBase
from ableton.v3.control_surface.components import \
    SessionNavigationComponent as SessionNavigationComponentBase
from ableton.v3.control_surface.components import SessionRingComponent
from ableton.v3.live import liveobj_valid, simple_track_name


class SessionNavigationComponent(SessionNavigationComponentBase):
    pass

    def set_horizontal_page_encoder(self, encoder):
        self._horizontal_paging.set_scroll_encoder(encoder)


class MixerSessionRingComponent(SessionRingComponent):
    pass

    def __init__(self, *a, **k):
        super().__init__(*a, name='Mixer_Session_Ring', num_tracks=8,
                         set_session_highlight=nop, is_private=True, **k)

    @listenable_property
    def controlled_range(self):
        tracks = self.tracks
        last_track = find_if(liveobj_valid, reversed(tracks))
        return 'Tracks {} to {}'.format(simple_track_name(tracks[0]),
                                        simple_track_name(last_track))

    def move(self, tracks, scenes):
        super().move(tracks, scenes)
        self.notify_controlled_range()
        self.notify(self.notifications.controlled_range, '',
                    self.controlled_range)


class MixerComponent(MixerComponentBase):
    pass

    def __init__(self, *a, **k):
        self._session_ring = MixerSessionRingComponent()
        super().__init__(*a, session_ring=self._session_ring, **k)
        self._session_navigation = SessionNavigationComponent(
            session_ring=self._session_ring, snap_track_offset=True,
            parent=self)
        self.add_children(self._session_ring)

    def set_track_bank_encoder(self, encoder):
        self._session_navigation.set_horizontal_page_encoder(encoder)
