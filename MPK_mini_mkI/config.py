# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MPK_mini_mkI/config.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 4634 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
 'STOP': -1, 
 'PLAY': -1, 
 'REC': -1, 
 'LOOP': -1, 
 'RWD': -1, 
 'FFWD': -1}
DEVICE_CONTROLS = (
 GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = ((-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                   (-1, -1))
TRACKARM_CONTROLS = (-1, -1, -1, -1, -1, -1, -1, -1)
BANK_CONTROLS = {
 'TOGGLELOCK': -1, 
 'BANKDIAL': -1, 
 'NEXTBANK': -1, 
 'PREVBANK': -1, 
 'BANK1': -1, 
 'BANK2': -1, 
 'BANK3': -1, 
 'BANK4': -1, 
 'BANK5': -1, 
 'BANK6': -1, 
 'BANK7': -1, 
 'BANK8': -1}
PAD_TRANSLATION = ((0, 0, 48, 9), (1, 0, 49, 9), (2, 0, 50, 9), (3, 0, 51, 9), (0, 1, 44, 9),
                   (1, 1, 45, 9), (2, 1, 46, 9), (3, 1, 47, 9), (0, 2, 40, 9), (1, 2, 41, 9),
                   (2, 2, 42, 9), (3, 2, 43, 9), (0, 3, 36, 9), (1, 3, 37, 9), (2, 3, 38, 9),
                   (3, 3, 39, 9))
CONTROLLER_DESCRIPTION = {
 'INPUTPORT': '"MPK mini"', 
 'OUTPUTPORT': '"MPK mini"', 
 'CHANNEL': -1, 
 'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {
 'NUMSENDS': 2, 
 'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1), 
 'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1), 
 'MASTERVOLUME': -1}
