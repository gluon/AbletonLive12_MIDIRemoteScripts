# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyFadr/KeyFadr.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 424 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from KeyPad import KeyPad

class KeyFadr(KeyPad):
    _encoder_range = list(range(80, 72, -1))
    _product_model_id = 102

    def __init__(self, *a, **k):
        (super(KeyFadr, self).__init__)(*a, **k)
