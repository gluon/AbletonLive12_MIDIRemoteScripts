# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/collection/indexed_dict.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1562 bytes
from __future__ import absolute_import, print_function, unicode_literals
from collections import OrderedDict

class IndexedDict(OrderedDict):

    def __init__(self, *args, **kwds):
        self._IndexedDict__keys = []
        (super(IndexedDict, self).__init__)(*args, **kwds)

    def __setitem__(self, key, value, *args, **kwds):
        (super(IndexedDict, self).__setitem__)(key, value, *args, **kwds)
        if key not in self._IndexedDict__keys:
            self._IndexedDict__keys.append(key)

    def __delitem__(self, key, *args, **kwds):
        (super(IndexedDict, self).__delitem__)(key, *args, **kwds)
        self._IndexedDict__keys.remove(key)

    def clear(self):
        super(IndexedDict, self).clear()
        self._IndexedDict__keys = []

    def popitem(self, last=True):
        item = super(IndexedDict, self).popitem(last)
        self._IndexedDict__keys.pop(-1 if last else 0)
        return item

    def keys(self):
        return self._IndexedDict__keys

    def item_by_index(self, ix):
        key = self._IndexedDict__keys[ix]
        return (key, self[key])

    def key_by_index(self, ix):
        return self._IndexedDict__keys[ix]

    def value_by_index(self, ix):
        return self[self._IndexedDict__keys[ix]]

    def index_by_key(self, key):
        return self._IndexedDict__keys.index(key)
