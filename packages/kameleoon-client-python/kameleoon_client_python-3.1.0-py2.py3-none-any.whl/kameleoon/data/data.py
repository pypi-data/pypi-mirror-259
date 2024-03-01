""" Kameleoon data module"""
from enum import IntEnum
from typing import Any, Dict


class DataType(IntEnum):
    """Data types"""

    CUSTOM_DATA = 0
    BROWSER = 1
    CONVERSION = 2
    DEVICE = 3
    PAGE_VIEW = 4
    USER_AGENT = 5
    ASSIGNED_VARIATION = 6


class BaseData:
    """Base data class"""

    @property
    def data_type(self) -> DataType:
        """Returns data type of the instance"""
        raise NotImplementedError

    def to_dict(self) -> Dict[str, Any]:
        """Convert class instance to dict"""
        return self.__dict__


class Data(BaseData):  # pylint: disable=W0223
    """Base external data class"""
