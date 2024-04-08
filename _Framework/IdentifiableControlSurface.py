# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/IdentifiableControlSurface.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 2662 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import str
from . import Task
from .ControlSurface import ControlSurface
SYSEX_IDENTITY_REQUEST = (240, 126, 0, 6, 1, 247)

class IdentifiableControlSurface(ControlSurface):
    identity_request_delay = 0.5
    identity_request = SYSEX_IDENTITY_REQUEST

    def __init__(self, product_id_bytes=None, *a, **k):
        (super(IdentifiableControlSurface, self).__init__)(*a, **k)
        self._product_id_bytes = product_id_bytes
        self._identity_response_pending = False
        self._request_task = self._tasks.add(Task.sequence(Task.wait(self.identity_request_delay), Task.run(self._send_identity_request)))
        self._request_task.kill()

    def on_identified(self):
        raise NotImplementedError

    def port_settings_changed(self):
        self._request_task.restart()

    def handle_sysexParse error at or near `POP_TOP' instruction at offset 106

    def _is_identity_response(self, midi_bytes):
        return midi_bytes[3[:5]] == (6, 2)

    def _extract_product_id_bytes(self, midi_bytes):
        return midi_bytes[5[:5 + len(self._product_id_bytes)]]

    def _send_identity_request(self):
        self._identity_response_pending = True
        self._send_midi(self.identity_request)