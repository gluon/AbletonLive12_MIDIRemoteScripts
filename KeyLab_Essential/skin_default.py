# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/skin_default.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1390 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color, SysexRGBColor

class Colors(object):

    class DefaultButton(object):
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)

    class Transport(object):
        PlayOn = Color(127)
        PlayOff = Color(0)
        StopOn = Color(127)
        StopOff = Color(0)

    class Session(object):
        ClipStopped = SysexRGBColor((31, 31, 0))
        ClipStarted = SysexRGBColor((0, 31, 0))
        ClipRecording = SysexRGBColor((31, 0, 0))
        ClipTriggeredPlay = SysexRGBColor((0, 31, 0))
        ClipTriggeredRecord = SysexRGBColor((31, 0, 0))
        ClipEmpty = SysexRGBColor((0, 0, 0))
        StopClip = Color(0)
        StopClipTriggered = Color(0)
        StopClipDisabled = Color(0)
        StoppedClip = Color(0)

    class Automation(object):
        On = Color(127)
        Off = Color(0)

    class View(object):
        Session = Color(0)
        Arranger = Color(127)

    class Mixer(object):
        MuteOn = Color(127)
        MuteOff = Color(0)
        SoloOn = Color(127)
        SoloOff = Color(0)
        ArmOn = Color(127)
        ArmOff = Color(0)


default_skin = Skin(Colors)
