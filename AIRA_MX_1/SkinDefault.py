# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/SkinDefault.py
# Compiled at: 2024-03-11 15:53:42
# Size of source mod 2**32: 697 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.Skin as Skin
from .Colors import Rgb

class Colors:

    class Session:
        ClipEmpty = Rgb.BLACK
        ClipStopped = Rgb.GREEN_HALF
        ClipStarted = Rgb.GREEN
        ClipRecording = Rgb.RED
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        NoScene = Rgb.BLACK
        Scene = Rgb.BLUE_HALF
        SceneTriggered = Rgb.BLUE_BLINK
        ScenePlaying = Rgb.BLUE
        StopClip = Rgb.RED
        StopClipTriggered = Rgb.RED_BLINK


def make_default_skin():
    return Skin(Colors)
