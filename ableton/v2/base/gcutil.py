# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/gcutil.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 1837 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.builtins import range
import gc
from collections import defaultdict
from .util import old_hasattr

def typename(obj):
    if old_hasattr(obj, "__class__"):
        return obj.__class__.__name__
    if old_hasattr(obj, "__name__"):
        return obj.__name__
    return "<unknown>"


def histogram(name_filter=None, objs=None):
    all_ = gc.get_objects() if objs is None else objs

    def _name_filter(name):
        return name_filter is None or name_filter in name

    hist = defaultdict((lambda: 0))
    for o in all_:
        n = typename(o)
        if _name_filter(n):
            hist[n] += 1

    return hist


def instances_by_name(name_filter):
    return [o for o in gc.get_objects() if name_filter == typename(o)]


def refget(objs, level=1):
    for _ in range(level):
        refs = (gc.get_referrers)(*objs)
        try:
            refs.remove(objs)
        except ValueError:
            pass

        objs = refs

    return refs
