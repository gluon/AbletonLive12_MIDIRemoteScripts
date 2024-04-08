# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/mode/mode.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 3143 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, nop, task
from . import LayerModeBase, Mode
from .modes import ModesComponent

class EnablingAddLayerMode(LayerModeBase):

    @depends(parent_task_group=None)
    def __init__(self, parent_task_group=None, *a, **k):
        (super().__init__)(*a, **k)
        self._should_track_layers = not isinstance(self._component, ModesComponent) and not hasattr(self._component, "disable_layer_tracking") and hasattr(self._component, "num_layers")
        if self._should_track_layers:
            self._possibly_disable_component_task = parent_task_group.add(task.run(self._possibly_disable_component))
            self._possibly_disable_component_task.kill()

    def enter_mode(self):
        component = self._get_component()
        self._layer.grab(component)
        if not component.is_enabled():
            component.set_enabled(True)

    def leave_mode(self):
        component = self._get_component()
        self._layer.release(component)
        if self._should_track_layers:
            self._possibly_disable_component_task.restart()

    def _possibly_disable_component(self):
        component = self._get_component()
        if not component.num_layers:
            component.set_enabled(False)


class CallFunctionMode(Mode):

    def __init__(self, on_enter_fn=nop, on_exit_fn=nop, *a, **k):
        (super().__init__)(*a, **k)
        self._on_enter_fn = on_enter_fn
        self._on_exit_fn = on_exit_fn

    def enter_mode(self):
        self._on_enter_fn()

    def leave_mode(self):
        self._on_exit_fn()


class ShowDetailClipMode(Mode):

    def __init__(self, application, *a, **k):
        (super().__init__)(*a, **k)
        self._view = application.view
        self._needs_restore_view = False

    def enter_mode(self):
        self._needs_restore_view = self._view.is_view_visible("Detail/DeviceChain", False)
        if self._needs_restore_view:
            self._view.show_view("Detail/Clip")

    def leave_mode(self):
        if self._needs_restore_view:
            self._view.show_view("Detail/DeviceChain")
        self._needs_restore_view = False
