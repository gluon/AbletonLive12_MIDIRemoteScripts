# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\colors.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.control_surface import BasicColors
from ableton.v3.control_surface.elements import FallbackColor, create_rgb_color
from ableton.v3.live import liveobj_color_to_midi_rgb_values


def create_color(r, g, b):
    return create_rgb_color((r, g, b, 0))


class Rgb:
    OFF = FallbackColor(create_color(0, 0, 0), BasicColors.OFF)
    WHITE_HALF = create_color(32, 32, 32)
    WHITE = FallbackColor(create_color(127, 127, 127), BasicColors.ON)
    RED = create_color(127, 0, 0)
    RED_HALF = create_color(32, 0, 0)
    RED_LOW = create_color(16, 0, 0)
    GREEN = create_color(0, 127, 0)
    GREEN_HALF = create_color(0, 32, 0)
    YELLOW = create_color(127, 72, 0)
    YELLOW_HALF = create_color(32, 24, 0)


class Skin:
    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class Transport:
        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_HALF
        StopOn = Rgb.WHITE
        StopOff = Rgb.WHITE_HALF
        LoopOn = Rgb.YELLOW
        LoopOff = Rgb.YELLOW_HALF
        MetronomeOn = Rgb.WHITE
        MetronomeOff = Rgb.WHITE_HALF
        TapTempoPressed = Rgb.WHITE
        TapTempo = Rgb.WHITE_HALF
        SeekPressed = Rgb.WHITE
        Seek = Rgb.WHITE_HALF
        CanCaptureMidi = Rgb.WHITE

    class Recording:
        ArrangementRecordOn = Rgb.RED
        ArrangementRecordOff = Rgb.RED_HALF
        SessionRecordOn = Rgb.RED
        SessionRecordOff = Rgb.RED_HALF

    class UndoRedo:
        UndoPressed = Rgb.WHITE
        Undo = Rgb.WHITE_HALF
        RedoPressed = Rgb.WHITE
        Redo = Rgb.WHITE_HALF

    class ClipActions:
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE

    class Session:
        Slot = Rgb.OFF
        SlotRecordButton = Rgb.RED_LOW
        NoSlot = Rgb.OFF
        ClipStopped = lambda x: create_color(
            *liveobj_color_to_midi_rgb_values(x))
        ClipTriggeredPlay = Rgb.GREEN_HALF
        ClipPlaying = Rgb.GREEN
        ClipTriggeredRecord = Rgb.RED_HALF
        ClipRecording = Rgb.RED
