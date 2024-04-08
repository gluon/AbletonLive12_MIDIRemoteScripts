# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/full_velocity_element.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 466 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .proxy_element import ProxyElement

class NullFullVelocity(object):
    enabled = False


class FullVelocityElement(ProxyElement):

    def __init__(self, full_velocity=None, *a, **k):
        super(FullVelocityElement, self).__init__(proxied_object=full_velocity,
          proxied_interface=(NullFullVelocity()))
