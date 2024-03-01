"""Kameleoon Configuration"""

from typing import Any, Dict, Optional
from kameleoon.configuration.feature_flag import FeatureFlag
from kameleoon.configuration.settings import Settings
from kameleoon.exceptions import FeatureNotFound, FeatureEnvironmentDisabled


class DataFile:
    """`DataFile` is a container for an actual client-configuration data"""

    @staticmethod
    def default(environment: Optional[str]) -> "DataFile":
        """Creates new instance of `DataFile` initialized with default values"""
        return DataFile(environment, Settings(), {})

    @staticmethod
    def from_json(environment: Optional[str], configuration: Dict[str, Any]) -> "DataFile":
        """Creates new instance of `DataFile` initialized from the specified configuration JSON"""
        settings = Settings(configuration.get("configuration"))
        feature_flags = {
            (feature_flag := FeatureFlag(jobj)).feature_key: feature_flag
            for jobj in configuration.get("featureFlags") or []
        }
        return DataFile(environment, settings, feature_flags)

    def __init__(self, environment: Optional[str], settings: Settings, feature_flags: Dict[str, FeatureFlag]) -> None:
        self.__environment = environment  # pylint: disable=W0238
        self.__settings = settings
        self.__feature_flags: Dict[str, FeatureFlag] = feature_flags
        self.__has_any_targeted_delivery_rule = any(
            rule.is_targeted_delivery
            for ff in self.__feature_flags.values()
            if ff.environment_enabled
            for rule in ff.rules
        )

    @property
    def settings(self) -> Settings:
        """Returns settings"""
        return self.__settings

    @property
    def feature_flags(self) -> Dict[str, FeatureFlag]:
        """Returns dictionary of all feature flags stored by feature keys"""
        return self.__feature_flags

    @property
    def has_any_targeted_delivery_rule(self) -> bool:
        """Returns `True` if has a feature flag with a rule of the targeted delivery type, otherwise returns `False`"""
        return self.__has_any_targeted_delivery_rule

    def get_feature_flag(self, feature_key: str) -> FeatureFlag:
        """
        Returns feature flag with the specified feature key if it exists,
        otherwise raises `FeatureNotFound` exception.
        """
        feature_flag = self.__feature_flags.get(feature_key)
        if feature_flag is None:
            raise FeatureNotFound(feature_key)
        if not feature_flag.environment_enabled:
            raise FeatureEnvironmentDisabled(feature_key, self.__environment)
        return feature_flag
