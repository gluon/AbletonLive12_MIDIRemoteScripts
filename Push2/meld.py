# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/meld.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 9893 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, find_if, listens, liveobj_valid
from ableton.v2.control_surface import EnumWrappingParameter, LiveObjectDecorator, NotifyingList, get_parameter_by_name
from .device_options import DeviceOnOffOption, DeviceSwitchOption, DeviceTriggerOption

class SelectedEngineType(int):
    pass


SelectedEngineType.a = SelectedEngineType(0)
SelectedEngineType.b = SelectedEngineType(1)

class UnisonVoicesType(int):
    pass


UnisonVoicesType.off = UnisonVoicesType(0)
UnisonVoicesType.two = UnisonVoicesType(1)
UnisonVoicesType.three = UnisonVoicesType(2)

class MonoPolyType(int):
    pass


MonoPolyType.mono = MonoPolyType(0)
MonoPolyType.poly = MonoPolyType(1)

class PolyVoicesType(int):
    pass


PolyVoicesType.two = PolyVoicesType(0)
PolyVoicesType.three = PolyVoicesType(1)
PolyVoicesType.four = PolyVoicesType(2)
PolyVoicesType.five = PolyVoicesType(3)
PolyVoicesType.six = PolyVoicesType(4)
PolyVoicesType.eight = PolyVoicesType(5)
PolyVoicesType.twelve = PolyVoicesType(6)

class MeldDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(MeldDeviceDecorator, self).__init__)(*a, **k)

        def get_parameter_by_original_name(name):
            return find_if((lambda p: p.original_name == name), self._live_object.parameters)

        class SelectedEnvelopeType(IntEnum):
            amp = 0
            mod = 1

        class SelectedLfoEffectType(IntEnum):
            effect1 = 0
            effect2 = 1

        class EnvelopeViewType(IntEnum):
            time = 0
            slope = 1

        self.osc_a_on_option = DeviceOnOffOption(name="Osc A",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineA_On")))
        self.osc_b_on_option = DeviceOnOffOption(name="Osc B",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineB_On")))
        self.filter_a_on_option = DeviceOnOffOption(name="Filter A",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineA_Filter_On")))
        self.filter_b_on_option = DeviceOnOffOption(name="Filter B",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineB_Filter_On")))
        selected_engine_provider = NotifyingList(available_values=[
         "A", "B"],
          default_value=(SelectedEngineType.a))
        self.selected_engine_parameter = EnumWrappingParameter(name="Selected Engine",
          parent=self,
          values_host=selected_engine_provider,
          index_property_host=(self._live_object),
          values_property="available_values",
          index_property="selected_engine",
          value_type=SelectedEngineType)
        self.selected_engine_option = DeviceSwitchOption(name="Selected Engine",
          parameter=(self.selected_engine_parameter),
          labels=[
         "A", "B"])
        self.envelope_switch_provider = NotifyingList(available_values=[
         "Amp", "Mod"],
          default_value=(SelectedEnvelopeType.amp))
        self.selected_envelope_parameter = EnumWrappingParameter(name="Selected Env",
          parent=self,
          values_host=(self.envelope_switch_provider),
          index_property_host=(self.envelope_switch_provider),
          values_property="available_values",
          index_property="index",
          value_type=SelectedEnvelopeType)
        self.lfo_effect_switch_provider = NotifyingList(available_values=[
         "Effect 1", "Effect 2"],
          default_value=(SelectedLfoEffectType.effect1))
        self.selected_lfo1_effect_parameter = EnumWrappingParameter(name="LFO1 Effect",
          parent=self,
          values_host=(self.lfo_effect_switch_provider),
          index_property_host=(self.lfo_effect_switch_provider),
          values_property="available_values",
          index_property="index",
          value_type=SelectedLfoEffectType)
        self.selected_lfo1_transformer_option = DeviceSwitchOption(name="LFO1 Effect",
          parameter=(self.selected_lfo1_effect_parameter),
          labels=[
         "FX 1", "FX 2"])
        self.amp_envelope_view_types_provider = NotifyingList(available_values=[
         "Time", "Slope"],
          default_value=(EnvelopeViewType.time))
        self.amp_envelope_view_parameter = EnumWrappingParameter(name="Envelope View",
          parent=self,
          values_host=(self.amp_envelope_view_types_provider),
          index_property_host=(self.amp_envelope_view_types_provider),
          values_property="available_values",
          index_property="index",
          value_type=EnvelopeViewType)
        self.unison_voices_provider = NotifyingList(available_values=[
         "Off", "2", "3"],
          default_value=(UnisonVoicesType.off))
        self.unison_voices_parameter = EnumWrappingParameter(name="Stack Voices",
          parent=self,
          values_host=(self.unison_voices_provider),
          index_property_host=(self._live_object),
          values_property="available_values",
          index_property="unison_voices",
          value_type=UnisonVoicesType)
        self.mono_poly_provider = NotifyingList(available_values=[
         "Mono", "Poly"],
          default_value=(MonoPolyType.mono))
        self.mono_poly_parameter = EnumWrappingParameter(name="Mono Poly",
          parent=self,
          values_host=(self.mono_poly_provider),
          index_property_host=(self._live_object),
          values_property="available_values",
          index_property="mono_poly",
          value_type=MonoPolyType)
        self.poly_voices_provider = NotifyingList(available_values=[
         '2', '3', '4', '5', '6', '8', '12'],
          default_value=(PolyVoicesType.eight))
        self.poly_voices_parameter = EnumWrappingParameter(name="Poly Voices",
          parent=self,
          values_host=(self.poly_voices_provider),
          index_property_host=(self._live_object),
          values_property="available_values",
          index_property="poly_voices",
          value_type=PolyVoicesType)
        self.link_envelopes_option = DeviceOnOffOption(name="Link Envelopes",
          property_host=(get_parameter_by_original_name("MeldVoice_LinkAmpEnvelopes")))
        self.lfo1_a_sync_option = DeviceOnOffOption(name="LFO 1 A Sync",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineA_Lfo1_Sync")))
        self.lfo1_a_retrigger_option = DeviceOnOffOption(name="LFO 1 A Retrigger",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineA_Lfo1_Retrigger")))
        self.lfo1_b_sync_option = DeviceOnOffOption(name="LFO 1 B Sync",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineB_Lfo1_Sync")))
        self.lfo1_b_retrigger_option = DeviceOnOffOption(name="LFO 1 B Retrigger",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineB_Lfo1_Retrigger")))
        self.lfo2_a_sync_option = DeviceOnOffOption(name="LFO 2 A Sync",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineA_Lfo2_Sync")))
        self.lfo2_b_sync_option = DeviceOnOffOption(name="LFO 2 B Sync",
          property_host=(get_parameter_by_original_name("MeldVoice_EngineB_Lfo2_Sync")))
        self.limiter_option = DeviceOnOffOption(name="Limiter",
          property_host=(get_parameter_by_original_name("MeldVoice_LimiterOn")))
        self.engine_a_glide_option = DeviceSwitchOption(name="Glide A",
          parameter=(get_parameter_by_original_name("MeldVoice_EngineA_GlideMode")),
          labels=[
         "Porta", "Gliss"])
        self.engine_b_glide_option = DeviceSwitchOption(name="Glide B",
          parameter=(get_parameter_by_original_name("MeldVoice_EngineB_GlideMode")),
          labels=[
         "Porta", "Gliss"])
        self._additional_parameters = (
         self.selected_engine_parameter,
         self.selected_envelope_parameter,
         self.selected_lfo1_effect_parameter,
         self.amp_envelope_view_parameter,
         self.unison_voices_parameter,
         self.mono_poly_parameter,
         self.poly_voices_parameter)
        self.register_disconnectables(self._additional_parameters)
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (
         self.osc_a_on_option,
         self.osc_b_on_option,
         self.filter_a_on_option,
         self.filter_b_on_option,
         self.selected_engine_option,
         self.link_envelopes_option,
         self.lfo1_a_sync_option,
         self.lfo1_a_retrigger_option,
         self.lfo1_b_sync_option,
         self.lfo1_b_retrigger_option,
         self.lfo2_a_sync_option,
         self.lfo2_b_sync_option,
         self.limiter_option,
         self.engine_a_glide_option,
         self.engine_b_glide_option,
         self.selected_lfo1_transformer_option)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters
