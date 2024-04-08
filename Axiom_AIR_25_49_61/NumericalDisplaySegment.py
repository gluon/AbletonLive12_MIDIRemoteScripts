# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/NumericalDisplaySegment.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1504 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.LogicalDisplaySegment as LogicalDisplaySegment

class NumericalDisplaySegment(LogicalDisplaySegment):

    @staticmethod
    def adjust_string(original, length):
        characters_to_retain = {
         '0': 48, 
         '1': 49, 
         '2': 50, 
         '3': 51, 
         '4': 52, 
         '5': 53, 
         '6': 54, 
         '7': 55, 
         '8': 56, 
         '9': 57}
        resulting_string = ""
        for char in original:
            if char in characters_to_retain:
                resulting_string = resulting_string + char

        if len(resulting_string) > length:
            resulting_string = resulting_string[None[:length]]
        if len(resulting_string) < length:
            resulting_string = resulting_string.rjust(length)
        return resulting_string

    def __init__(self, width, update_callback):
        LogicalDisplaySegment.__init__(self, width, update_callback)

    def display_string(self):
        resulting_string = " " * int(self._width)
        if self._data_source != None:
            resulting_string = NumericalDisplaySegment.adjust_string(self._data_source.display_string(), self._width)
        return resulting_string
