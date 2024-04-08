# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/skin.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2225 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface.elements import Color
LIVE_COLOR_TABLE_INDEX_OFFSET = 8
ON_COLOR = Color(127)
OFF_COLOR = Color(0)

class ColorsBase(object):

    class DefaultButton(object):
        On = ON_COLOR
        Off = OFF_COLOR
        Disabled = OFF_COLOR

    class Mixer(object):
        SoloOn = Color(2)
        SoloOff = OFF_COLOR
        MuteOn = Color(1)
        MuteOff = OFF_COLOR
        ArmOff = OFF_COLOR
        CrossfadeAssignA = Color(1)
        CrossfadeAssignB = Color(3)

    class Session(object):
        RecordButton = ON_COLOR
        ClipTriggeredPlay = Color(3)
        ClipTriggeredRecord = Color(6)
        ClipStarted = Color(4)
        ClipRecording = Color(7)
        ClipStopped = Color(2)
        ClipSelected = Color(127)
        Scene = Color(0)
        SceneTriggered = Color(1)
        NoScene = OFF_COLOR
        StopClipTriggered = ON_COLOR
        StopClip = Color(4)
        StopClipDisabled = OFF_COLOR
        ClipEmpty = OFF_COLOR
        ClipEmptyWithStopButton = Color(1)
        SceneOff = OFF_COLOR
        SceneOn = Color(2)
        SceneDefault = Color(21)

    class Action(object):
        Available = OFF_COLOR
        On = Color(1)
        Off = Color(0)
        QuantizeOn = Color(5)
        QuantizeOff = Color(0)

    class Transport(object):
        PlayOn = ON_COLOR
        PlayOff = OFF_COLOR
        StopOn = ON_COLOR
        StopOff = OFF_COLOR
        MetronomeOn = Color(6)
        MetronomeOff = Color(0)
        TapTempo = Color(1)

    class Recording(object):
        On = ON_COLOR
        Off = OFF_COLOR
        Transition = ON_COLOR

    class Automation(object):
        On = Color(2)
        Off = OFF_COLOR

    class Navigation(object):
        Enabled = Color(1)

    class Background(object):
        On = Color(1)

    class Mode(object):
        On = Color(1)
        Off = OFF_COLOR


class ForceColors(ColorsBase):

    class Mixer(ColorsBase.Mixer):
        ArmOn = Color(3)


class MPCColors(ColorsBase):

    class Mixer(ColorsBase.Mixer):
        ArmOn = Color(1)
