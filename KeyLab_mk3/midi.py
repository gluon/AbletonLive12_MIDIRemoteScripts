from ableton.v3.control_surface.midi import SYSEX_END, SYSEX_START
from .display import BUTTON_TYPES, Color, Icon, ScreenId

# Define headers
SYSEX_HEADER = (SYSEX_START, 0, 32, 107, 127, 66)
LED_HEADER = SYSEX_HEADER + (4, 2, 3)
DISPLAY_HEADER = SYSEX_HEADER + (0, 2, 4)

# Connection messages
make_connection_message = lambda parameter_byte: SYSEX_HEADER + (
0, 2, 5, parameter_byte, SYSEX_END)

CONNECTION_MESSAGE = make_connection_message(1)
DISCONNECTION_MESSAGE = make_connection_message(0)

# ID mappings
BUTTON_ID_TO_SYSEX_ID = {20: 7, 21: 6, 22: 5, 23: 4, 24: 8, 25: 9, 26: 10,
    27: 11, 41: 15, 42: 14, 43: 13, 44: 12}

PAD_ID_TO_SYSEX_ID = {0: 82, 1: 83, 2: 84, 3: 85, 4: 86, 5: 87, 6: 88, 7: 89,
    8: 90, 9: 91, 10: 92, 11: 93}

# Touch IDs
ENCODER_TOUCH_IDS = (8, 9, 10, 11, 12, 13, 14, 15, 38)
FADER_TOUCH_IDS = (28, 29, 30, 31, 32, 34, 35, 36, 37)


# Function definitions
def make_parameter_screen(screen_id, name, value_as_str, value):
    pass
    return DISPLAY_HEADER + (screen_id,) + (0,) + value_as_str + (
    0, 1) + name + (0, 2, value, 0) + (4,) + Color.BLUE + (0, SYSEX_END)


def make_button_segment(button_index, text=None,
    button_type=BUTTON_TYPES['icon'][0], color=Color.WHITE, icon=Icon.NONE):
    pass
    return DISPLAY_HEADER + (button_index,) + (0, button_type,) + (
    0, 3, icon) + (0, 4) + color + (0, 5) + (text if text else (0,)) + (
    0, SYSEX_END)


def make_two_line_screen(line_1, line_2, color=Color.WHITE):
    pass
    return DISPLAY_HEADER + (ScreenId.TWO_LINE,) + make_line_bytes(line_1,
                                                                   color) + make_line_bytes(
        line_2, Color.WHITE, address=3) + (SYSEX_END,)


def make_popup_screen(line_1, line_2, line_3=None,
    colors=(Color.WHITE, Color.WHITE, Color.WHITE), icon=Icon.NONE):
    pass
    return DISPLAY_HEADER + (
    ScreenId.THREE_LINE_POPUP if line_3 else ScreenId.ICONIFIED_TWO_LINE_POPUP if icon else ScreenId.TWO_LINE_POPUP,) + make_line_bytes(
        line_1, colors[0]) + make_line_bytes(line_2, colors[1], address=3) + (
        (make_line_bytes(line_3, colors[2], address=6)) if line_3 else ()) + (
        (6, icon, 0,) if line_3 is None else ()) + (SYSEX_END,)


def make_line_bytes(line, color, address=0):
    pass
    return (address,) + line + (0, address + 2) + color + (0,)
