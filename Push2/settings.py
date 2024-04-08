# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/settings.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 689 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.setting import OnOffSetting

def create_settings(preferences=None):
    preferences = preferences if preferences is not None else {}
    return {'workflow':OnOffSetting(name="Workflow",
       value_labels=[
      "Scene", "Clip"],
       default_value=True,
       preferences=preferences), 
     'aftertouch_mode':OnOffSetting(name="Pressure",
       value_labels=[
      "Mono", "Polyphonic"],
       default_value=True,
       preferences=preferences)}
