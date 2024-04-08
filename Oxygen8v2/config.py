# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen8v2/config.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3838 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
 'STOP': GENERIC_STOP, 
 'PLAY': GENERIC_PLAY, 
 'REC': GENERIC_REC, 
 'LOOP': GENERIC_LOOP, 
 'RWD': GENERIC_RWD, 
 'FFWD': GENERIC_FFWD, 
 'NORELEASE': 0}
DEVICE_CONTROLS = (
 GENERIC_ENC1,
 GENERIC_ENC2,
 GENERIC_ENC3,
 GENERIC_ENC4,
 GENERIC_ENC5,
 GENERIC_ENC6,
 GENERIC_ENC7,
 GENERIC_ENC8)
VOLUME_CONTROLS = GENERIC_SLIDERS
TRACKARM_CONTROLS = (
 GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {
 'TOGGLELOCK': GENERIC_BUT9, 
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
CONTROLLER_DESCRIPTION = {'INPUTPORT':"USB Oxygen 8 v2", 
 'OUTPUTPORT':"USB Oxygen 8 v2", 
 'CHANNEL':0}
MIXER_OPTIONS = {
 'NUMSENDS': 2, 
 'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1), 
 'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1), 
 'MASTERVOLUME': -1}
