# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/button_matrix.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1431 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import slicer, to_slice
from ableton.v2.control_surface.elements import ButtonMatrixElement as ButtonMatrixElementBase
from ...base import lazy_attribute, recursive_map
from ..display import Renderable

class ButtonMatrixElement(ButtonMatrixElementBase, Renderable):

    @property
    @slicer(2)
    def submatrix(self, col_slice, row_slice):
        col_slice = to_slice(col_slice)
        row_slice = to_slice(row_slice)
        rows = [row[col_slice] for row in self._orig_buttons[row_slice]]
        return ButtonMatrixElement(rows=rows)

    @lazy_attribute
    def renderable_state(self):
        if not any((isinstance(button, Renderable) for row in self._orig_buttons for button in row)):
            return
        matrix = recursive_map((lambda button:         if isinstance(button, Renderable):
button.renderable_state # Avoid dead code: None), self._orig_buttons)
        if len(matrix) == 1:
            return matrix[0]
        return matrix
