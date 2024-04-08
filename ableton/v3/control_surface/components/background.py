# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/background.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 4615 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from .. import Component
from ..controls import ButtonControl, InputControl, RadioButtonGroup

class NopControl(InputControl):

    class State(InputControl.State):

        def _event_listener_required(self):
            return True


class BackgroundComponent(Component):

    def __init__(self, name='Background', control_type=None, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._control_type = control_type or NopControl

    def _setup_control_state(self, name, control_state):
        pass

    def __getattr__(self, name):
        if name.startswith("set_"):
            return partial(self._set_element_for_control, name[4[:None]])
        raise AttributeError(name)

    def _set_element_for_control(self, name, element):
        if element:
            element.reset()
        elif name in self.__dict__:
            self.__dict__[name].set_control_element(element)
        else:
            control = self._control_type()
            control_state = control._get_state(self)
            setattr(self, name, control_state)
            self._setup_control_state(name, control_state)
            control_state.set_control_element(element)


class TranslatingBackgroundComponent(BackgroundComponent):
    channel_selection_buttons = RadioButtonGroup(unchecked_color="Translation.Channel.NotSelected",
      checked_color="Translation.Channel.Selected")

    def __init__(self, name='Translating_Background', translation_channel=0, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._base_translation_channel = translation_channel

    def set_channel_selection_buttons(self, buttons):
        self.channel_selection_buttons.set_control_element(buttons)
        if buttons:
            if self.channel_selection_buttons.checked_index < 0:
                self.channel_selection_buttons.checked_index = 0

    @channel_selection_buttons.checked
    def channel_selection_buttons(self, button):
        for control_state in self._control_states.values():
            control_state.channel = self._base_translation_channel + button.index

    def _setup_control_state(self, _, control_state):
        control_state.channel = self._base_translation_channel


class ModifierBackgroundComponent(BackgroundComponent):

    def __init__(self, name='Modifier_Background', *a, **k):
        (super().__init__)(a, name=name, control_type=ButtonControl, **k)

    def _setup_control_state(self, name, control_state):
        base_name = self.name.title().replace("_", "")
        control_name = name.title().replace("_", "")
        control_state.color = "{}.{}".format(base_name, control_name)
        control_state.pressed_color = "{}.{}Pressed".format(base_name, control_name)
