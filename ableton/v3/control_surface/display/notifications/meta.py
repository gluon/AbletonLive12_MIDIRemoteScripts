# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/meta.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2425 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from inspect import getmro
from typing import Callable
from .type_decl import Notification, _DefaultText, _TransformDefaultText

def transform_notification(default: "Notification", transform_fn: "Callable[[str], str]"):
    if not callable(default):
        return transform_fn(default)

    def notification_fn(*a, **k):
        return transform_fn(default(*a, **k))

    return notification_fn


def update_special_attributes(cls, exclude_by_default=True):
    base_class = getmro(cls)[-2]
    for name, value in vars(base_class).items():
        subclass_value = vars(cls).get(name, None)
        if subclass_value is None:
            if isinstance(value, type):
                subclass_value = type(name, (value,), {})
                setattr(cls, name, subclass_value)
            else:
                if isinstance(subclass_value, type):
                    include_all = getattr(subclass_value, "INCLUDE_ALL", False)
                    update_special_attributes(subclass_value, False if include_all else exclude_by_default)
            if name.startswith("__") or exclude_by_default:
                if subclass_value is None:
                    setattr(cls, name, None)
            if subclass_value is None or isinstance(subclass_value, _DefaultText):
                setattr(cls, name, getattr(base_class, name))
            elif isinstance(subclass_value, _TransformDefaultText):
                setattr(cls, name, transform_notification(getattr(base_class, name), subclass_value.transform_fn))


class DefaultNotificationsMeta(type):

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        update_special_attributes(new_cls)
        return new_cls
