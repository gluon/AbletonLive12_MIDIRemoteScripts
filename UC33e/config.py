# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/UC33e/config.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 4352 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
 'STOP': GENERIC_STOP, 
 'PLAY': GENERIC_PLAY, 
 'REC': GENERIC_REC, 
 'LOOP': GENERIC_LOOP, 
 'RWD': GENERIC_RWD, 
 'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = (
 (
  GENERIC_ENC1, 0),
 (
  GENERIC_ENC2, 1),
 (
  GENERIC_ENC3, 2),
 (
  GENERIC_ENC4, 3),
 (
  GENERIC_ENC5, 4),
 (
  GENERIC_ENC6, 5),
 (
  GENERIC_ENC7, 6),
 (
  GENERIC_ENC8, 7))
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, 0),
 (
  GENERIC_SLI2, 1),
 (
  GENERIC_SLI3, 2),
 (
  GENERIC_SLI4, 3),
 (
  GENERIC_SLI5, 4),
 (
  GENERIC_SLI6, 5),
 (
  GENERIC_SLI7, 6),
 (
  GENERIC_SLI8, 7))
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
 'NEXTBANK': GENERIC_PAD5, 
 'PREVBANK': GENERIC_PAD1, 
 'BANK1': -1, 
 'BANK2': -1, 
 'BANK3': -1, 
 'BANK4': -1, 
 'BANK5': -1, 
 'BANK6': -1, 
 'BANK7': -1, 
 'BANK8': -1}
CONTROLLER_DESCRIPTIONS = {'INPUTPORT':"UC-33 USB MIDI Controller (Port 1)", 
 'OUTPUTPORT':"UC-33 USB MIDI Controller (Port 1)", 
 'CHANNEL':0}
MIXER_OPTIONS = {
 'NUMSENDS': 2, 
 'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1), 
 'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1), 
 'MASTERVOLUME': 28}
