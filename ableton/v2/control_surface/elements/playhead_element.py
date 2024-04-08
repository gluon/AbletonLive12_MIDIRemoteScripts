# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/playhead_element.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 681 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import nop
from .proxy_element import ProxyElement

class NullPlayhead(object):
    notes = []
    start_time = 0.0
    step_length = 1.0
    velocity = 0.0
    wrap_around = False
    track = None
    clip = None
    set_feedback_channels = nop


class PlayheadElement(ProxyElement):

    def __init__(self, playhead=None, *a, **k):
        super(PlayheadElement, self).__init__(proxied_object=playhead,
          proxied_interface=(NullPlayhead()))

    def reset(self):
        self.track = None
