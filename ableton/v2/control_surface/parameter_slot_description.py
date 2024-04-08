# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/parameter_slot_description.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 6428 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import const
from ..base import EventObject, find_if, listenable_property, listens_group, liveobj_valid
RESULTING_NAME_KEY = "ResultingName"
DISPLAY_NAME_TRANSFORMER_KEY = "DisplayNameTransformer"
CONDITION_NAME_KEY = "ConditionName"
CONDITIONS_LIST_NAME_KEY = "ConditionsListName"
PREDICATE_KEY = "Predicate"
OPERAND_NAME_KEY = "Operand"
AND = "and"
OR = "or"

def find_parameter(name, host):
    parameters = host.parameters if liveobj_valid(host) else []
    return find_if((lambda p: p.original_name == name), parameters)


class ParameterSlotDescription(EventObject):
    __events__ = ('content', )

    def __init__(self, *a, **k):
        (super(ParameterSlotDescription, self).__init__)(*a, **k)
        self._parameter_host = None
        self._default_parameter_name = ""
        self._display_name_transformer = None
        self._conditions = []
        self._cached_content = (None, None)

    def _calc_content(self):
        parameter_name = self._default_parameter_name
        display_name_transformer = self._display_name_transformer
        for condition in self._conditions:
            result = True
            for subcond in condition[CONDITIONS_LIST_NAME_KEY]:
                result = eval("%s %s %s" % (
                 result,
                 subcond[OPERAND_NAME_KEY],
                 subcond[PREDICATE_KEY](find_parameter(subcond[CONDITION_NAME_KEY], self._parameter_host))))
                if not result:
                    continue

            if result:
                parameter_name = condition[RESULTING_NAME_KEY]
                display_name_transformer = condition[DISPLAY_NAME_TRANSFORMER_KEY]
                break

        return (
         parameter_name, display_name_transformer)

    @listens_group("value")
    def __on_condition_value_changed(self, _parameter):
        new_content = self._calc_content()
        if new_content != self._cached_content:
            self._cached_content = new_content
            self.notify_content()

    def set_parameter_host(self, host):
        self._parameter_host = host
        self._cached_content = self._calc_content()
        params_names = set()
        for c in self._conditions:
            params_names.update([cond[CONDITION_NAME_KEY] for cond in c[CONDITIONS_LIST_NAME_KEY]])

        self._ParameterSlotDescription__on_condition_value_changed.replace_subjects([find_parameter(name, self._parameter_host) for name in params_names])

    def if_parameter(self, parameter_name):
        self._conditions.append({RESULTING_NAME_KEY: (self._default_parameter_name), 
         DISPLAY_NAME_TRANSFORMER_KEY: (self._display_name_transformer), 
         CONDITIONS_LIST_NAME_KEY: [
                                    {CONDITION_NAME_KEY: parameter_name, OPERAND_NAME_KEY: AND}]})
        self._default_parameter_name = ""
        self._display_name_transformer = None
        return self

    def chain_condition(self, operand, parameter_name):
        self._conditions[-1][CONDITIONS_LIST_NAME_KEY].append({CONDITION_NAME_KEY: parameter_name, OPERAND_NAME_KEY: operand})
        return self

    def and_parameter(self, parameter_name):
        return self.chain_condition(AND, parameter_name)

    def or_parameter(self, parameter_name):
        return self.chain_condition(OR, parameter_name)

    def _add_condition_predicate(self, predicate):
        self._conditions[-1][CONDITIONS_LIST_NAME_KEY][-1][PREDICATE_KEY] = predicate

    def has_value(self, value):
        self._add_condition_predicate(lambda p: str(p) == value)
        return self

    def has_value_in(self, values):
        self._add_condition_predicate(lambda p: str(p) in values)
        return self

    def does_not_have_value(self, value):
        self._add_condition_predicate(lambda p: str(p) != value)
        return self

    def is_available(self, value):
        self._add_condition_predicate(lambda p: liveobj_valid(p) == value)
        return self

    def else_use(self, parameter_name):
        self._default_parameter_name = parameter_name
        self._display_name_transformer = None
        return self

    def with_name(self, display_name):
        self._display_name_transformer = const(display_name)
        return self

    def with_name_transformer(self, func):
        self._display_name_transformer = func
        return self

    @listenable_property
    def display_name_transformer(self):
        return self._cached_content[1]

    def __str__(self):
        return self._cached_content[0]


def use(parameter_name):
    return ParameterSlotDescription().else_use(parameter_name)
