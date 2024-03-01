"""Exclusive Campaign condition"""
from typing import Any, Union, Dict
from kameleoon.data.manager.assigned_variation import AssignedVariation
from kameleoon.targeting.conditions.targeting_condition import TargetingCondition


class ExclusiveExperiment(TargetingCondition):
    """ExclusiveExperiment represents Exclusive Campaign condition from back-office"""

    def __init__(self, json_condition: Dict[str, Union[str, int, Any]]):
        super().__init__(json_condition)

    def check(self, data: Any) -> bool:
        """Need to return true if variation storage is empty or
        it has only single current experiment in the storage
        """
        if isinstance(data, tuple) and (len(data) == 2):
            current_experiment_id, variation_storage = data
            if isinstance(current_experiment_id, int) and isinstance(variation_storage, dict):
                return self.__check(current_experiment_id, variation_storage)
        return False

    @staticmethod
    def __check(current_experiment_id: int, variation_storage: Dict[int, AssignedVariation]) -> bool:
        return (len(variation_storage) == 0) or \
            ((len(variation_storage) == 1) and (current_experiment_id in variation_storage))
