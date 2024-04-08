# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control_XL/SkinDefault.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1013 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from _Framework.ButtonElement import Color
import _Framework.Skin as Skin

class Defaults(object):

    class DefaultButton(object):
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)


class BiLedColors(object):

    class Mixer(object):
        SoloOn = Color(60)
        SoloOff = Color(28)
        MuteOn = Color(29)
        MuteOff = Color(47)
        ArmSelected = Color(15)
        ArmUnselected = Color(13)
        TrackSelected = Color(62)
        TrackUnselected = Color(29)
        NoTrack = Color(0)
        Sends = Color(47)
        Pans = Color(60)

    class Device(object):
        Parameters = Color(13)
        NoDevice = Color(0)
        BankSelected = Color(15)
        BankUnselected = Color(0)


def make_default_skin():
    return Skin(Defaults)


def make_biled_skin():
    return Skin(BiLedColors)
