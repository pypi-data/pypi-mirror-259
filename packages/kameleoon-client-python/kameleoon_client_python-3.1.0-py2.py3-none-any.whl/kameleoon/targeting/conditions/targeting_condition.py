"""Base class for all conditions"""

from enum import Enum
import logging
from typing import Any, TypeVar, Union, Dict

from kameleoon.data.data import Data
from kameleoon.helpers.logger import Logger

T = TypeVar("T", bound=Data)  # pylint: disable=C0103


class TargetingConditionType(Enum):
    """Targeting condition types"""

    CUSTOM_DATUM = "CUSTOM_DATUM"
    TARGET_EXPERIMENT = "TARGET_EXPERIMENT"
    EXCLUSIVE_EXPERIMENT = "EXCLUSIVE_EXPERIMENT"
    DEVICE_TYPE = "DEVICE_TYPE"
    VISITOR_CODE = "VISITOR_CODE"
    PAGE_URL = "PAGE_URL"
    PAGE_TITLE = "PAGE_TITLE"
    CONVERSIONS = "CONVERSIONS"
    SDK_LANGUAGE = "SDK_LANGUAGE"
    BROWSER = "BROWSER"
    EXPLICIT_TRIGGER = "EXPLICIT_TRIGGER"
    UNKNOWN = "UNKNOWN"


class TargetingCondition:
    """Condition is a base class for all SDK conditions"""

    NON_EXISTENT_IDENTIFIER = -1

    def __init__(self, json_condition: Dict[str, Union[str, Any]]):
        self.type = json_condition.get("targetingType")
        self.include = json_condition.get("isInclude", True) is not False

    def check(self, data: Any) -> bool:
        """Check the condition for targeting"""
        raise NotImplementedError

    @property
    def _logger(self) -> logging.Logger:
        """Get logger for targeting condition"""
        return Logger.shared()
