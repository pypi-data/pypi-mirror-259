"""Kameleoon Client Configuration"""

import os
from logging import Logger
from typing import Any, Dict, Optional
import yaml
from kameleoon.helpers.logger import Logger as KLogger
from kameleoon.exceptions import ConfigCredentialsInvalid, ConfigFileNotFound


DEFAULT_REFRESH_INTERVAL_MINUTES = 60
DEFAULT_SESSION_DURATION_MINUTES = 30
DEFAULT_DEFAULT_TIMEOUT_MILLISECONDS = 10_000
DEFAULT_CONFIGURATION_PATH = "/etc/kameleoon/client-python.yaml"


class KameleoonClientConfig:
    """Client configuration which can be used instead of external configuration file"""

    # pylint: disable=R0913
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        refresh_interval_minute=DEFAULT_REFRESH_INTERVAL_MINUTES,
        session_duration_minute=DEFAULT_SESSION_DURATION_MINUTES,
        default_timeout_millisecond=DEFAULT_DEFAULT_TIMEOUT_MILLISECONDS,
        environment: Optional[str] = None,
        top_level_domain="",
        logger: Optional[Logger] = None,
        multi_threading=False,
    ) -> None:
        if not client_id:
            raise ConfigCredentialsInvalid("Client ID is not specified")
        if not client_secret:
            raise ConfigCredentialsInvalid("Client secret is not specified")
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__logger = logger or KLogger.shared()
        self.__refresh_interval_second = 0.0
        self.set_refresh_interval_minute(refresh_interval_minute)
        self.__session_duration_second = 0.0
        self.set_session_duration_minute(session_duration_minute)
        self.__default_timeout_second = 0.0
        self.set_default_timeout_millisecond(default_timeout_millisecond)
        self.__environment: Optional[str] = None
        self.set_environment(environment)
        self.__top_level_domain = ""
        self.set_top_level_domain(top_level_domain)
        self.__multi_threading = False
        self.set_multi_threading(multi_threading)

    @staticmethod
    def read_from_yaml(config_path=DEFAULT_CONFIGURATION_PATH) -> "KameleoonClientConfig":
        """
        Loads `KameleoonClientConfig` object from an SDK configuration file.

        A configuration file's fields with improper names or values are ignored.

        :param config_path: Path to a configuration file; the default value is '/etc/kameleoon/client-python.yaml'
        :type config_path: str

        :return: Loaded `KameleoonClientConfig` object
        :rtype: KameleoonClientConfig

        :raises ConfigFileNotFound: Indicates that a configuration file with the passed config path is not found
        """
        if not os.path.exists(config_path):
            raise ConfigFileNotFound(f"No config file {config_path} or config object is found")
        with open(config_path, "r", encoding="utf-8") as yaml_file:
            config_dict: Dict[str, Any] = yaml.load(yaml_file, Loader=yaml.SafeLoader)
        client_id: str = config_dict.get("client_id", "1")
        client_secret: str = config_dict.get("client_secret", "2")
        kwargs: Dict[str, Any] = {}
        if isinstance(refresh_interval_minute := config_dict.get("refresh_interval_minute"), (int, float)):
            kwargs["refresh_interval_minute"] = float(refresh_interval_minute)
        if isinstance(session_duration_minute := config_dict.get("session_duration_minute"), (int, float)):
            kwargs["session_duration_minute"] = float(session_duration_minute)
        if isinstance(default_timeout_millisecond := config_dict.get("default_timeout_millisecond"), int):
            kwargs["default_timeout_millisecond"] = default_timeout_millisecond
        if isinstance(environment := config_dict.get("environment"), str):
            kwargs["environment"] = environment
        if isinstance(top_level_domain := config_dict.get("top_level_domain"), str):
            kwargs["top_level_domain"] = top_level_domain
        if isinstance(multi_threading := config_dict.get("multi_threading"), bool):
            kwargs["multi_threading"] = multi_threading
        return KameleoonClientConfig(client_id, client_secret, **kwargs)

    @property
    def client_id(self) -> str:
        """Returns the client ID"""
        return self.__client_id

    @property
    def client_secret(self) -> str:
        """Returns the client secret"""
        return self.__client_secret

    @property
    def logger(self) -> Logger:
        """Returns the logger instance"""
        return self.__logger

    def set_logger(self, value: Logger) -> None:
        """Sets the logger instance"""
        self.__logger = value

    @property
    def refresh_interval_second(self) -> float:
        """Returns the refresh interval in seconds"""
        return self.__refresh_interval_second

    def set_refresh_interval_minute(self, value: float) -> None:
        """Sets the refresh interval in minutes"""
        if value <= 0:
            self._log("Configuration refresh interval must have positive value. Default refresh "
                      f"interval ({DEFAULT_REFRESH_INTERVAL_MINUTES} minutes) is applied.")
            value = DEFAULT_REFRESH_INTERVAL_MINUTES
        self.__refresh_interval_second = value * 60.0

    @property
    def session_duration_second(self) -> float:
        """Returns the session duration in seconds"""
        return self.__session_duration_second

    def set_session_duration_minute(self, value: float) -> None:
        """Sets the session duration in minutes"""
        if value <= 0:
            self._log("Session duration must have positive value. Default session duration "
                      f"({DEFAULT_SESSION_DURATION_MINUTES} minutes) is applied.")
            value = DEFAULT_SESSION_DURATION_MINUTES
        self.__session_duration_second = value * 60.0

    @property
    def default_timeout_second(self) -> float:
        """Returns the default timeout in seconds"""
        return self.__default_timeout_second

    def set_default_timeout_millisecond(self, value: int) -> None:
        """Sets the default timeout in milliseconds"""
        if value <= 0:
            self._log("Default timeout must have positive value. Default value "
                      f"({DEFAULT_DEFAULT_TIMEOUT_MILLISECONDS} ms) is applied.")
            value = DEFAULT_DEFAULT_TIMEOUT_MILLISECONDS
        self.__default_timeout_second = value / 1000.0

    @property
    def environment(self) -> Optional[str]:
        """Returns the environment"""
        return self.__environment

    def set_environment(self, value: Optional[str]) -> None:
        """Sets the environment"""
        self.__environment = value

    @property
    def top_level_domain(self) -> str:
        """Returns the top level domain"""
        return self.__top_level_domain

    def set_top_level_domain(self, value: str) -> None:
        """Sets the top level domain"""
        if not value:
            self._log("Setting top level domain is strictly recommended, "
                      "otherwise you may have problems when using subdomains.")
        self.__top_level_domain = value

    @property
    def multi_threading(self) -> bool:
        """Returns the multi_threading flag state"""
        return self.__multi_threading

    def set_multi_threading(self, value: bool) -> None:
        """Sets the multi_threading flag state"""
        self.__multi_threading = value

    def _log(self, message: str) -> None:
        self.logger.warning(message)
