# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\mode_buttons.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable


class ModeButtonsComponent(Component, Renderable):
    pass
    device_button = ButtonControl()
    mixer_button = ButtonControl()

    def __init__(self, *a, **k):
        super().__init__(*a, name='Mode_Buttons', **k)
