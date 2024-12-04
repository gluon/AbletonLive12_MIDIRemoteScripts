# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\elements.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from functools import partial

from ableton.v3.control_surface import MIDI_NOTE_TYPE, ElementsBase, MapMode, \
    create_button, create_encoder, create_matrix_identifiers, \
    create_sysex_sending_button
from ableton.v3.control_surface.elements import CachingSendMessageGenerator, \
    DisplayLineElement, TouchElement
from . import midi
from .display import Line1Text, Line2Text, ScreenId


def create_rgb_button(identifier, name=None, **k):
    return create_sysex_sending_button(identifier, name, midi.LED_HEADER + (
    midi.BUTTON_ID_TO_SYSEX_ID[identifier],), is_rgb=True, **k)


def create_rgb_pad(identifier, name, **k):
    return create_sysex_sending_button(identifier, name, midi.LED_HEADER + (
    midi.PAD_ID_TO_SYSEX_ID[identifier],), msg_type=MIDI_NOTE_TYPE, is_rgb=True,
                                       **k)


def create_continuous_control(identifier, name, **k):
    return create_encoder(identifier, name,
                          map_mode=MapMode.Absolute if identifier >= 105 else MapMode.LinearBinaryOffset,
                          **k)


class Elements(ElementsBase):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.add_modifier_button(45, 'Context_Button_0')
        self.add_modifier_button(46, 'Context_Button_1')
        self.add_button(20, 'Stop_Button')
        self.add_button(21, 'Play_Button')
        self.add_button(22, 'Record_Button')
        self.add_button(23, 'Tap_Button')
        self.add_button(24, 'Loop_Button')
        self.add_button(25, 'Rewind_Button')
        self.add_button(26, 'Fastforward_Button')
        self.add_button(27, 'Metronome_Button')
        self.add_button(40, 'Back_Button')
        self.add_button(41, 'Save_Button')
        self.add_button(42, 'Quantize_Button')
        self.add_button(43, 'Undo_Button')
        self.add_button(44, 'Redo_Button')
        for i in range(2, 8):
            self.add_button(45 + i, 'Context_Button_{}'.format(i))
        self.add_matrix(create_matrix_identifiers(0, 12, width=4), 'Pads',
                        element_factory=create_rgb_pad, channels=9)
        self.add_encoder(104, 'Encoder_8', map_mode=MapMode.LinearBinaryOffset)
        self.add_encoder(113, 'Fader_8')
        self.add_encoder(116, 'Display_Encoder',
                         map_mode=MapMode.LinearBinaryOffset)
        self.add_modified_control(control=self.display_encoder,
                                  modifier=self.context_button_0)
        self.add_modified_control(control=self.display_encoder,
                                  modifier=self.context_button_1)
        self.add_matrix(
            [[91, 92, 94, 95, 96, 97, 102, 103] + list(range(105, 113))],
            'Continuous_Controls', element_factory=create_continuous_control)
        self.add_submatrix(self.continuous_controls, 'Encoders', columns=(0, 8))
        self.add_submatrix(self.continuous_controls, 'Faders', columns=(8, 16))
        self.add_matrix([midi.ENCODER_TOUCH_IDS + midi.FADER_TOUCH_IDS],
                        'Parameter_Touch_Elements',
                        element_factory=self.create_touch_element)
        self.add_sysex_element(midi.DISPLAY_HEADER,
                               'Display_Full_Screen_Command',
                               send_message_generator=CachingSendMessageGenerator(
                                   midi.make_two_line_screen), optimized=True)
        self.display_line_1 = DisplayLineElement(name='Display_Line_1',
                                                 display_fn=lambda
                                                     message: self.display_full_screen_command.send_value(
                                                     line_1=message),
                                                 default_formatting=Line1Text())
        self.display_line_2 = DisplayLineElement(name='Display_Line_2',
                                                 display_fn=lambda
                                                     message: self.display_full_screen_command.send_value(
                                                     line_2=message),
                                                 default_formatting=Line2Text())
        self.add_sysex_element(midi.DISPLAY_HEADER + (ScreenId.TWO_LINE_POPUP,),
                               'Display_Popup_Command',
                               send_message_generator=midi.make_popup_screen)
        self.add_sysex_element(
            midi.DISPLAY_HEADER + (ScreenId.ENCODER_PARAMETER,),
            "Display_Parameter_Command",
            send_message_generator=midi.make_parameter_screen, optimized=True, )
        for i in range(8):
            self.add_sysex_element(midi.DISPLAY_HEADER + (i + 1,),
                'Display_Button_Command_{}'.format(i),
                send_message_generator=partial(midi.make_button_segment, i + 1),
                optimized=True, )

    def add_button(self, identifier, name, **k):
        self.add_element(name,
                         create_rgb_button if identifier in midi.BUTTON_ID_TO_SYSEX_ID else create_button,
                         identifier, **k)

    def create_touch_element(self, identifier, **k):
        # Determine the control type based on the identifier
        if identifier == 38:
            host_control = self.encoder_8
        elif identifier == 37:
            host_control = self.fader_8
        elif identifier in midi.ENCODER_TOUCH_IDS:
            host_control = self.continuous_controls_raw[
                midi.ENCODER_TOUCH_IDS.index(identifier)]
        else:
            host_control = self.continuous_controls_raw[
                midi.FADER_TOUCH_IDS.index(identifier) + 8]

        # Return a TouchElement instance
        return TouchElement(identifier, encoder=host_control, **k)
