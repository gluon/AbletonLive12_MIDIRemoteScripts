# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/disconnectable.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2483 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .util import find_if

class Disconnectable(object):

    def disconnect(self):
        pass


class CompoundDisconnectable(Disconnectable):

    def __init__(self, *a, **k):
        (super(CompoundDisconnectable, self).__init__)(*a, **k)
        self._registered_disconnectables = []

    def register_disconnectables(self, disconnectables):
        for disconnectable in disconnectables:
            self.register_disconnectable(disconnectable)

        return disconnectables

    def register_disconnectable(self, slot):
        if slot not in self._registered_disconnectables:
            self._registered_disconnectables.append(slot)
        return slot

    def unregister_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)

    def disconnect_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)
            slot.disconnect()

    def find_disconnectable(self, predicate):
        return find_if(predicate, self._registered_disconnectables)

    def has_disconnectable(self, slot):
        return slot in self._registered_disconnectables

    def disconnect(self):
        for slot in self._registered_disconnectables:
            slot.disconnect()

        self._registered_disconnectables = []
        super(CompoundDisconnectable, self).disconnect()


class disconnectable(object):

    def __init__(self, managed=None, *a, **k):
        (super(disconnectable, self).__init__)(*a, **k)
        self._managed = managed

    def __enter__(self):
        managed = self._managed
        return managed

    def __exit__(self, *a, **k):
        if self._managed is not None:
            self._managed.disconnect()
