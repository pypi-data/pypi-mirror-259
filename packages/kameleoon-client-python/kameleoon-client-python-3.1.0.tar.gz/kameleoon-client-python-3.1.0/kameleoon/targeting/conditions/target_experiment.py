"""Experiment condition"""
from typing import Any, Union, Dict
from kameleoon.data.manager.assigned_variation import AssignedVariation
from kameleoon.exceptions import NotFoundError
from kameleoon.targeting.conditions.targeting_condition import TargetingCondition
from kameleoon.targeting.conditions.constants import TargetingOperator


class TargetExperiment(TargetingCondition):
    """TargetExperiment represents Experiment condition from back-office"""

    def __init__(self, json_condition: Dict[str, Union[str, int, Any]]):
        super().__init__(json_condition)
        experiment_id_name = "experiment"
        self.experiment_id = int(json_condition.get(experiment_id_name, TargetingCondition.NON_EXISTENT_IDENTIFIER))
        if self.experiment_id == TargetingCondition.NON_EXISTENT_IDENTIFIER:
            raise NotFoundError(experiment_id_name)
        try:
            self.__variation = json_condition.get("variation")
            self.__operator = TargetingOperator[str(json_condition["variationMatchType"])]
        except KeyError as ex:
            self._logger.error("%s has wrong JSON structure: %s", self.__class__, ex)

    def check(self, data: Any) -> bool:
        return isinstance(data, dict) and self._check(data)

    def _check(self, variation_storage: Dict[int, AssignedVariation]) -> bool:
        if self.__operator == TargetingOperator.EXACT:
            as_variation = variation_storage.get(self.experiment_id)
            return isinstance(as_variation, AssignedVariation) and (as_variation.variation_id == self.__variation)
        if self.__operator == TargetingOperator.ANY:
            return len(variation_storage) > 0
        return False
