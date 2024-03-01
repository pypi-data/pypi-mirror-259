"""Client for Kameleoon"""
import asyncio
import itertools
import time
from http.cookies import Morsel
from typing import cast, Callable, Coroutine, Optional, Tuple, Union, Any, List, Dict

from kameleoon.kameleoon_client_config import KameleoonClientConfig
from kameleoon.client_readiness.async_readiness import AsyncClientReadiness
from kameleoon.client_readiness.threading_readiness import ThreadingClientReadiness
from kameleoon.configuration.data_file import DataFile
from kameleoon.configuration.feature_flag import FeatureFlag
from kameleoon.configuration.rule import Rule
from kameleoon.configuration.rule_type import RuleType
from kameleoon.configuration.variation import Variation
from kameleoon.configuration.variation_by_exposition import VariationByExposition
from kameleoon.helpers.visitor_code import validate_visitor_code
from kameleoon.hybrid.hybrid_manager_impl import HybridManagerImpl
from kameleoon.managers.warehouse.warehouse_manager import WarehouseManager

from kameleoon.data.manager.assigned_variation import AssignedVariation
from kameleoon.data.manager.visitor import Visitor
from kameleoon.data.manager.visitor_manager import VisitorManager
from kameleoon.network.access_token_source_factory import AccessTokenSourceFactory
from kameleoon.network.activity_event import ActivityEvent
from kameleoon.network.sendable import Sendable
from kameleoon.network.net_provider_impl import NetProviderImpl
from kameleoon.network.net_provider import Response
from kameleoon.network.network_manager_factory import NetworkManagerFactory
from kameleoon.network.network_manager_factory_impl import NetworkManagerFactoryImpl
from kameleoon.network.services.configuration_service import ConfigurationService
from kameleoon.network.services.data_service import DataService
from kameleoon.network.cookie.cookie_manager import CookieManager

from kameleoon.data import Conversion, CustomData, Data
from kameleoon.helpers.multi_threading import (
    ThreadEventLoop,
    run_in_thread,
    invoke_coro,
    get_loop,
    has_running_event_loop,
)
from kameleoon.helpers.repeat_timer import RepeatTimer
from kameleoon.helpers.scheduler import Scheduler
from kameleoon.real_time.real_time_configuration_service import (
    RealTimeConfigurationService,
)
from kameleoon.targeting.conditions.sdk_language_condition import SdkLanguageCondition
from kameleoon.sdk_version import SdkVersion

from kameleoon.exceptions import (
    FeatureVariationNotFound,
    FeatureVariableNotFound,
    FeatureEnvironmentDisabled,
    SiteCodeIsEmpty,
)
from kameleoon.helpers.functions import obtain_hash_double_rule, enum_from_literal
from kameleoon.targeting.conditions.targeting_condition import TargetingConditionType

__all__ = [
    "KameleoonClient",
]

REFERENCE = 0
X_PAGINATION_PAGE_COUNT = "X-Pagination-Page-Count"
SEGMENT = "targetingSegment"
KAMELEOON_TRACK_EXPERIMENT_THREAD = "KameleoonTrackExperimentThread"
KAMELEOON_TRACK_DATA_THREAD = "KameleoonTrackDataThread"
STATUS_ACTIVE = "ACTIVE"
FEATURE_STATUS_DEACTIVATED = "DEACTIVATED"
# pylint: disable=W0511
HYBRID_EXPIRATION_TIME = 5.0  # TODO: hybrid manager timeout is less than call timeout; affects on sync-monothread mode


# pylint: disable=R0904
class KameleoonClient:
    """
    KameleoonClient

    Example:

    .. code-block:: python3

        from kameleoon import KameleoonClientFactory
        from kameleoon import KameleoonClientConfig

        SITE_CODE = 'a8st4f59bj'

        kameleoon_client = KameleoonClientFactory.create(SITE_CODE)

        kameleoon_client = KameleoonClientFactory.create(SITE_CODE,
                                                         config_path='/etc/kameleoon/client-python.yaml')

        kameleoon_client_config = KameleoonClientConfig('client_id', 'client_secret')
        kameleoon_client = KameleoonClientFactory.create(SITE_CODE, kameleoon_client_config)
    """

    _network_manager_factory: NetworkManagerFactory = NetworkManagerFactoryImpl()

    # pylint: disable=R0913
    def __init__(self, site_code: str, config: KameleoonClientConfig) -> None:
        """
        This initializer should not be called explicitly. Use `KameleoonClientFactory.create` instead.

        :param site_code: Code of the website you want to run experiments on. This unique code id can
                              be found in our platform's back-office. This field is mandatory.
        :type site_code: str
        :param config: Configuration object which can be used instead of external file at configuration_path.
                                This field is optional set to None by default.
        :type config: KameleoonClientConfig

        :raises SiteCodeIsEmpty: Indicates that the specified site code is empty string which is invalid value
        """
        # pylint: disable=too-many-instance-attributes
        # Eight is reasonable in this case.
        if not site_code:
            raise SiteCodeIsEmpty("Provided site_code is empty")
        self.site_code = site_code
        self._config = config
        self._real_time_configuration_service: Optional[RealTimeConfigurationService] = None
        self._update_configuration_handler: Optional[Callable[[], None]] = None
        self._scheduler = Scheduler(config.logger)
        self.__add_fetch_configuration_job()
        self._threading_readiness = ThreadingClientReadiness()
        self._async_readiness = AsyncClientReadiness(self._threading_readiness)
        self._data_file: DataFile = DataFile.default(config.environment)
        self._visitor_manager = VisitorManager(config.session_duration_second, self._scheduler)
        self._hybrid_manager = HybridManagerImpl(HYBRID_EXPIRATION_TIME)

        self._cookie_manager = CookieManager(config.top_level_domain)
        atsf = AccessTokenSourceFactory(config.client_id, config.client_secret)
        self._network_manager = self._network_manager_factory.create(
            self.site_code, config.environment, config.default_timeout_second, NetProviderImpl(), atsf, config.logger
        )
        self._warehouse_manager = WarehouseManager(self._network_manager, self._visitor_manager, config.logger)
        self._thread_event_loop = ThreadEventLoop() if config.multi_threading else None

        self._timer: Optional[RepeatTimer] = self._scheduler.timer()
        self._timer.setDaemon(True)
        self._timer.start()

        self._init_fetch_configuration()

    def __del__(self):
        self._clear_timer()
        try:
            if self._thread_event_loop:
                self._thread_event_loop.run_coro(self._network_manager.net_provider.close())
                self._thread_event_loop.stop()
            else:
                invoke_coro(self._network_manager.net_provider.close())
        except AttributeError:
            pass

    ###
    #   Public API methods
    ###

    def wait_init_async(self) -> Coroutine[Any, Any, bool]:
        """
        Asynchronously waits for the initialization of the Kameleoon client.
        This method allows you to pause the execution of your code until the client is initialized.

        :return: A coroutine that returns a flag indicating if the initialization process has succeeded
        :rtype: Coroutine[Any, Any, bool]
        """
        return self._async_readiness.wait()

    def wait_init(self) -> bool:
        """
        Synchronously waits for the initialization of the Kameleoon client.
        This method allows you to pause the execution of your code until the client is initialized.

        :return: A flag indicating if the initialization process has succeeded
        :rtype: bool
        """
        return self._threading_readiness.wait()

    def get_visitor_code(
        self,
        cookies_readonly: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, Morsel[str]]] = None,
        default_visitor_code: Optional[str] = None,
    ) -> str:
        """
        Reads and updates visitor code in cookies. Possible optional parameters:
        - `Dict[str, str]` (e.g. `request.COOKIES`). It's recommended to use in conjunction
        with `KameleoonWSGIMiddleware`
        - `http.cookies.SimpleCookie` (see https://docs.python.org/3/library/http.cookies.html)

        The method updates the cookies with a new visitor code if it's needed in case of `http.cookies.SimpleCookie`
        is passed.

        If the cookies does not contain a visitor code, a new visitor code is set to the `default_visitor_code`
        if it is specified, otherwise a new visitor code is randomly generated.

        :param cookies_readonly: Readonly dictionary (usually, request.COOKIES) which would not be modified.
        Should be used in conjunction with `KameleoonWSGIMiddleware` service.
        :type cookies_readonly: Optional[Dict[str, str]]
        :param cookies: Mutable dictionary (usually, `http.cookies.SimpleCookie`) which will be filled during method
        call.
        Should be used if you want to manage cookies manually (without KameleoonWSGIMiddleware service).
        :type cookies: Dict[str, Morsel[str]]
        :param default_visitor_code: Visitor code to be used if no visitor code in cookies
        :type default_visitor_code: Optional[str]
        :return: The visitor code
        :rtype: str

        Example:

        .. code-block:: python3
            visitor_code = kameleoon_client.get_visitor_code(cookies_readonly=request.COOKIES)
            # or
            simple_cookies = SimpleCookie()
            simple_cookies.load(cookie_header)

            visitor_code = kameleoon_client.get_visitor_code(cookies=simple_cookies)

            cookie_header = simple_cookies.output()
        """
        return self._cookie_manager.get_or_add(cookies_readonly, cookies, default_visitor_code)

    def set_legal_consent(
        self, visitor_code: str, consent: bool, cookies: Optional[Dict[str, Morsel[str]]] = None
    ) -> None:
        """
        Sets or updates the legal consent status for a visitor identified by their unique visitor code,
        affecting values in the cookies based on the consent status.

        This method allows you to set or update the legal consent status for a specific visitor
        identified by their visitor code and adjust values in the cookies accordingly. The legal
        consent status is represented by a boolean value, where 'True' indicates consent, and 'False'
        indicates a withdrawal or absence of consent. Depending on the consent status, various values in
        the cookies may be affected.

        :param visitor_code: The unique visitor code identifying the visitor.
        :type visitor_code: str
        :param consent: A boolean value representing the legal consent status.
        :type consent: bool
        :param cookies: Request-respose cookies. Optional parameter.
        :type cookies: Optional[Dict[str, Morsel[str]]]

        Example:

        .. code-block:: python3
        # Set legal consent for a specific visitor and adjust cookie values accordingly
        kameeloon_client.set_legal_consent("visitor123", True)

        # Update legal consent for another visitor and modify cookie values based on the consent status
        kameeloon_client.set_legal_consent("visitor456", False)

        # Set legal consent for a specific visitor and adjust cookie values accordingly
        kameeloon_client.set_legal_consent("visitor123", True, cookies)

        # Update legal consent for another visitor and modify cookie values based on the consent status
        kameeloon_client.set_legal_consent("visitor456", False, cookies)
        """
        validate_visitor_code(visitor_code)
        visitor = self._visitor_manager.get_or_create_visitor(visitor_code)
        visitor.legal_consent = consent
        if cookies is not None:
            self._cookie_manager.update(visitor_code, consent, cookies)

    def add_data(self, visitor_code: str, *args) -> None:
        """
        To associate various data with the current user, we can use the add_data() method.
        This method requires the visitor_code as a first parameter, and then accepts several additional parameters.
        These additional parameters represent the various Data Types allowed in Kameleoon.

        Note that the add_data() method doesn't return any value and doesn't interact with the Kameleoon back-end
        servers by itself. Instead, all declared data is saved for further sending via the flush() method described
        in the next paragraph. This reduces the number of server calls made, as data is usually grouped
        into a single server call triggered by the execution of flush()

        :param visitor_code: Unique identifier of the user. This field is mandatory.
        :type visitor_code: str
        :param args:
        :return: None

        Examples:

        .. code-block:: python

                from kameleoon.data import PageView

                visitor_code = kameleoon_client.get_visitor_code(request.COOKIES)
                kameleoon_client.add_data(visitor_code, CustomData("test-id", "test-value"))
                kameleoon_client.add_data(visitor_code, Browser(BrowserType.CHROME))
                kameleoon_client.add_data(visitor_code, PageView("www.test.com", "test-title"))
                kameleoon_client.add_data(visitor_code, Conversion(1, 100.0))
                kameleoon_client.add_data(visitor_code, Interest(1))
        """
        validate_visitor_code(visitor_code)
        visitor = self._visitor_manager.get_or_create_visitor(visitor_code)
        visitor.add_data(*args, logger=self._config.logger)
        self._config.logger.debug("Successfully added data")

    def track_conversion(self, visitor_code: str, goal_id: int, revenue: float = 0.0) -> None:
        """
        To track conversion, use the track_conversion() method. This method requires visitor_code and goal_id to track
        conversion on this particular goal. In addition, this method also accepts revenue as a third optional argument
        to track revenue. The visitor_code is usually identical to the one that was used when triggering the experiment.
        The track_conversion() method doesn't return any value. This method is non-blocking as the server
        call is made asynchronously.

        :param visitor_code: Unique identifier of the user. This field is mandatory.
        :type visitor_code: str
        :param goal_id: ID of the goal. This field is mandatory.
        :type goal_id: int
        :param revenue: Revenue of the conversion. This field is optional.
        :type revenue: float
        :return: None
        """
        validate_visitor_code(visitor_code)
        self.add_data(visitor_code, Conversion(goal_id, revenue))
        self.flush(visitor_code)

    def flush(self, visitor_code: Optional[str] = None):
        """
        Data associated with the current user via add_data() method is not immediately sent to the server.
        It is stored and accumulated until it is sent automatically by the trigger_experiment()
        or track_conversion() methods, or manually by the flush() method.
        This allows the developer to control exactly when the data is flushed to our servers. For instance,
        if you call the add_data() method a dozen times, it would be a waste of ressources to send data to the
        server after each add_data() invocation. Just call flush() once at the end.
        The flush() method doesn't return any value. This method is non-blocking as the server call
        is made asynchronously.


        :param visitor_code: Unique identifier of the user. This field is mandatory.
        :type visitor_code: Optional[str]

        Examples:

        .. code-block:: python

                from kameleoon.data import PageView

                visitor_code = kameleoon_client.get_visitor_code(request.COOKIES)
                kameleoon_client.add_data(visitor_code, CustomData("test-id", "test-value"))
                kameleoon_client.add_data(visitor_code, Browser(BrowserType.CHROME))
                kameleoon_client.add_data(visitor_code, PageView("www.test.com", "test-title"))
                kameleoon_client.add_data(visitor_code, Conversion(1, 100.0))
                kameleoon_client.add_data(visitor_code, Interest(1))

                kameleoon_client.flush()

        """
        if visitor_code is not None:
            validate_visitor_code(visitor_code)
            visitor = self._visitor_manager.get_visitor(visitor_code)
            self.__send_tracking_request(visitor_code, visitor)
        else:
            for visitor_code in self._visitor_manager:  # pylint: disable=R1704
                visitor = self._visitor_manager.get_visitor(visitor_code)
                self.__send_tracking_request(visitor_code, visitor, False)

    def is_feature_active(self, visitor_code: str, feature_key: str) -> bool:
        """
        Check if feature is active for a given visitor code

        This method takes a visitor_code and feature_key (or feature_id) as mandatory arguments to check
        if the specified feature will be active for a given user.
        If such a user has never been associated with this feature flag, the SDK returns a boolean
        value randomly (true if the user should have this feature or false if not). If a user with a given visitor_code
        is already registered with this feature flag, it will detect the previous feature flag value.
        You have to make sure that proper error handling is set up in your code as shown in the example to the right
        to catch potential exceptions.


        :param visitor_code: str Unique identifier of the user. This field is mandatory.
        :param feature_key: str Key of the feature flag you want to expose to a user. This field is mandatory.
        :return: bool Value of the feature that is active for a given visitor_code.


        :raises:
            FeatureNotFound: Exception indicating that the requested feature ID has not been found in
                                          the internal configuration of the SDK. This is usually normal and means that
                                          the feature flag has not yet been activated on Kameleoon's side
                                          (but code implementing the feature is already deployed on the
                                          web-application's side).
            VisitorCodeInvalid: Raise when the provided visitor code is not valid
                        (empty, or longer than 255 characters)

        Examples:

        .. code-block:: python3

                visitor_code = kameleoon_client.get_visitor_code(request.COOKIES)
                feature_key = "new_checkout"
                has_new_checkout = False

                try:
                    has_new_checkout = kameleoon_client.is_feature_active(visitor_code, feature_key)
                except FeatureNotFound:
                    # The user will not be counted into the experiment, but should see the reference variation
                    logger.debug(...)

                if has_new_checkout:
                    # Implement new checkout code here
        """
        try:
            (_, variation_key) = self.__get_feature_variation_key(visitor_code, feature_key)
            return variation_key != Variation.Type.OFF.value
        except FeatureEnvironmentDisabled:
            return False

    def get_feature_variation_variables(self, feature_key: str, variation_key: str) -> Dict[str, Any]:
        """
        Retrieve all feature variables.
        A feature variables can be changed easily via our web application.

        :param feature_key: str Key of the feature you want to obtain to a user.
                            This field is mandatory.
        :return: Dictionary of feature variables
        :rtype: Dict[str, Any]

        :raises: FeatureNotFound: Exception indicating that the requested feature Key has not been found
                                               in the internal configuration of the SDK. This is usually normal and
                                               means that the feature flag has not yet been activated on
                                               Kameleoon's side.
                 FeatureVariationNotFound: Variation key isn't found for current feature flag.

        Example:

        .. code-block:: python3
                try:
                    data = kameleoon_client.get_feature_variation_variables(feature_key)
                except FeatureNotFound:
                    # The feature is not yet activated on Kameleoon's side
                except FeatureVariationNotFound:
                    # The variation key is not found for current feature flag
                    pass
        """

        # pylint: disable=no-else-raise
        feature_flag = self._data_file.get_feature_flag(feature_key)
        variation = feature_flag.get_variation(variation_key)
        if not variation:
            raise FeatureVariationNotFound(variation_key)
        variables: Dict[str, Any] = {}
        for var in variation.variables:
            variables[var.key] = var.get_value()
        return variables

    async def get_remote_data_async(self, key: str, timeout: Optional[float] = None) -> Optional[Any]:
        """
        The get_remote_data_async method allows you to retrieve data asynchronously (according to a key passed as
        argument) stored on a remote Kameleoon server. Usually data will be stored on our remote servers
        via the use of our Data API. This method, along with the availability of our highly scalable servers
        for this purpose, provides a convenient way to quickly store massive amounts of data that
        can be later retrieved for each of your visitors / users.

        :param key: key you want to retrieve data. This field is mandatory.
        :type key: str
        :param timeout: requests Timeout for request (in seconds). Equals default_timeout in a config file.
        This field is optional.
        :type timeout: Optional[float]

        :return: data assosiated with this key, decoded into json
        :rtype: Optional[Any]
        """
        service: DataService = self._network_manager.get_service(DataService)
        response = await service.get_remote_data(key, timeout)
        return response.content

    def get_remote_data(self, key: str, timeout: Optional[float] = None) -> Optional[Any]:
        """
        The get_remote_data method allows you to retrieve data (according to a key passed as
        argument) stored on a remote Kameleoon server. Usually data will be stored on our remote servers
        via the use of our Data API. This method, along with the availability of our highly scalable servers
        for this purpose, provides a convenient way to quickly store massive amounts of data that
        can be later retrieved for each of your visitors / users.

        :param key: key you want to retrieve data. This field is mandatory.
        :type key: str
        :param timeout: requests Timeout for request (in seconds). Equals default_timeout in a config file.
        This field is optional.
        :type timeout: Optional[float]

        :return: data assosiated with this key, decoded into json
        :rtype: Optional[Any]
        """
        service: DataService = self._network_manager.get_service(DataService)
        coro = service.get_remote_data(key, timeout, sync=self.__is_sync_mode())
        response = cast(Response, self.__make_sync_call_anyway(coro, "get_remote_data"))
        return response.content

    async def get_remote_visitor_data_async(
        self, visitor_code: str, add_data=True, timeout: Optional[float] = None
    ) -> List[Data]:
        """
        The get_remote_visitor_data_async is an asynchronous method for retrieving custom data for
        the latest visit of `visitor_code` from Kameleoon Data API and optionally adding it
        to the storage so that other methods could decide whether the current visitor is targeted or not.

        :param visitor_code: The visitor code for which you want to retrieve the assigned data. This field is mandatory.
        :type visitor_code: str
        :param add_data: A boolean indicating whether the method should automatically add retrieved data for a visitor.
        If not specified, the default value is `True`. This field is optional.
        :type add_data: bool
        :param timeout: requests Timeout for request (in seconds). Equals default_timeout in a config file.
        This field is optional.
        :type timeout: Optional[float]

        :return: A list of data assigned to the given visitor.
        :rtype: List[Data]
        """
        service: DataService = self._network_manager.get_service(DataService)
        response = await service.get_remote_visitor_data(visitor_code, timeout)
        return self.__handle_remote_visitor_data_response(response, visitor_code, add_data)

    def get_remote_visitor_data(self, visitor_code: str, add_data=True, timeout: Optional[float] = None) -> List[Data]:
        """
        The get_remote_visitor_data is a synchronous method for retrieving custom data for
        the latest visit of `visitor_code` from Kameleoon Data API and optionally adding it
        to the storage so that other methods could decide whether the current visitor is targeted or not.

        :param visitor_code: The visitor code for which you want to retrieve the assigned data. This field is mandatory.
        :type visitor_code: str
        :param add_data: A boolean indicating whether the method should automatically add retrieved data for a visitor.
        If not specified, the default value is `True`. This field is optional.
        :type add_data: bool
        :param timeout: requests Timeout for request (in seconds). Equals default_timeout in a config file.
        This field is optional.
        :type timeout: Optional[float]

        :return: A list of data assigned to the given visitor.
        :rtype: List[Data]
        """
        service: DataService = self._network_manager.get_service(DataService)
        coro = service.get_remote_visitor_data(visitor_code, timeout, sync=self.__is_sync_mode())
        response = self.__make_sync_call_anyway(coro, "get_remote_visitor_data")
        if response is None:
            return []
        return self.__handle_remote_visitor_data_response(response, visitor_code, add_data)

    def __handle_remote_visitor_data_response(
        self, response: Response, visitor_code: str, add_data: bool
    ) -> List[Data]:
        if response.content is None:
            return []
        data_list = self.__parse_custom_data_list(response.content)
        if add_data:
            self.add_data(visitor_code, *data_list)
        return data_list

    def __parse_custom_data_list(self, raw: Any) -> List[Data]:
        try:
            latest_record = raw.get("currentVisit")
            if latest_record is None:
                previous_visits = raw.get("previousVisits")
                if previous_visits:
                    latest_record = previous_visits[0]
                else:
                    return []
            return [
                CustomData(jcd.get("index", -1), *jcd.get("valuesCountMap", []))
                for event in latest_record.get("customDataEvents", [])
                if (jcd := event.get("data"))
            ]
        except Exception as ex:  # pylint: disable=W0703
            self._config.logger.error(f"Parsing of visitor data failed: {ex}")
            return []

    def get_visitor_warehouse_audience_async(
        self,
        visitor_code: str,
        custom_data_index: int,
        warehouse_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> Coroutine[Any, Any, Optional[CustomData]]:
        """
        Asynchronously retrieves data associated with a visitor's warehouse audiences and adds it to the visitor.
        Retrieves all audience data associated with the visitor in your data warehouse using the specified
        `visitor_code` and `warehouse_key`. The `warehouse_key` is typically your internal user ID.
        The `custom_data_index` parameter corresponds to the Kameleoon custom data that Kameleoon uses to target your
        visitors. You can refer to the
        <a href="https://help.kameleoon.com/warehouse-audience-targeting/">warehouse targeting documentation</a>
        for additional details. The method returns a `CustomData` object, confirming
        that the data has been added to the visitor and is available for targeting purposes.

        :param visitor_code: A unique visitor identification string, can't exceed 255 characters length.
        This field is mandatory.
        :type visitor_code: str
        :param custom_data_index: An integer representing the index of the custom data you want to use to target
        your BigQuery Audiences. This field is mandatory.
        :type custom_data_index: int
        :param warehouse_key: A key to identify the warehouse data, typically your internal user ID.
        This field is optional.
        :type warehouse_key: Optional[str]
        :param timeout: requests Timeout for request (in seconds). Equals default_timeout in a config file.
        This field is optional.
        :type timeout: Optional[float]

        :return: A `CustomData` instance confirming that the data has been added to the visitor.
        :rtype: Optional[CustomData]

        :raises:
            VisitorCodeInvalid: Raise when the provided visitor code is not valid (empty, or longer than 255 characters)
        """
        return self._warehouse_manager.get_visitor_warehouse_audience(
            visitor_code, custom_data_index, warehouse_key, timeout
        )

    def get_visitor_warehouse_audience(
        self,
        visitor_code: str,
        custom_data_index: int,
        warehouse_key: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> Optional[CustomData]:
        """
        Synchronously retrieves data associated with a visitor's warehouse audiences and adds it to the visitor.
        Retrieves all audience data associated with the visitor in your data warehouse using the specified
        `visitor_code` and `warehouse_key`. The `warehouse_key` is typically your internal user ID.
        The `custom_data_index` parameter corresponds to the Kameleoon custom data that Kameleoon uses to target your
        visitors. You can refer to the
        <a href="https://help.kameleoon.com/warehouse-audience-targeting/">warehouse targeting documentation</a>
        for additional details. The method returns a `CustomData` object, confirming
        that the data has been added to the visitor and is available for targeting purposes.

        :param visitor_code: A unique visitor identification string, can't exceed 255 characters length.
        This field is mandatory.
        :type visitor_code: str
        :param custom_data_index: An integer representing the index of the custom data you want to use to target
        your BigQuery Audiences. This field is mandatory.
        :type custom_data_index: int
        :param warehouse_key: A key to identify the warehouse data, typically your internal user ID.
        This field is optional.
        :type warehouse_key: Optional[str]
        :param timeout: requests Timeout for request (in seconds). Equals default_timeout in a config file.
        This field is optional.
        :type timeout: Optional[float]

        :return: A `CustomData` instance confirming that the data has been added to the visitor.
        :rtype: Optional[CustomData]

        :raises:
            VisitorCodeInvalid: Raise when the provided visitor code is not valid (empty, or longer than 255 characters)
        """
        coro = self._warehouse_manager.get_visitor_warehouse_audience(
            visitor_code, custom_data_index, warehouse_key, timeout, sync=self.__is_sync_mode()
        )
        return self.__make_sync_call_anyway(coro, "get_visitor_warehouse_audience")

    def get_feature_list(self) -> List[str]:
        """
        The get_feature_list method uses for obtaining a list of feature flag IDs:
        - currently available for the SDK

        :return: List of all feature flag IDs
        :rtype: List[int]
        """
        return list(self._data_file.feature_flags)

    def get_active_feature_list_for_visitor(self, visitor_code: str) -> List[str]:
        """
        The get_active_feature_list_for_visitor method uses for obtaining a list of feature flag IDs:
        - currently targeted and active simultaneously for a visitor

        :param visitor_code: unique identifier of a visitor
        :type visitor_code: Optional[str]

        :return: List of all feature flag IDs or targeted and active simultaneously
                 for current visitorCode
        :rtype: List[int]
        """

        def filter_conditions(feature_flag: FeatureFlag) -> bool:
            (variation, rule) = self.__calculate_variation_rule_for_feature(visitor_code, feature_flag)
            variation_key = self.__calculate_variation_key(variation, rule, feature_flag)
            return variation_key != Variation.Type.OFF.value

        return list(
            map(
                lambda feature_flag: feature_flag.feature_key,
                filter(
                    filter_conditions,
                    self._data_file.feature_flags.values(),
                ),
            )
        )

    def get_feature_variation_key(self, visitor_code: str, feature_key: str) -> str:
        """
        Returns a variation key for visitor code

        This method takes a visitor_code and feature_key as mandatory arguments and
        returns a variation assigned for a given visitor
        If such a user has never been associated with any feature flag rules, the SDK returns a default variation key
        You have to make sure that proper error handling is set up in your code as shown in the example
        to the right to catch potential exceptions.

        :param visitor_code: unique identifier of a visitor
        :type visitor_code: str
        :param feature_key: unique identifier of feature flag
        :type feature_key: str

        :return: Returns a variation key for visitor code
        :rtype: str

        :raises:
            FeatureNotFound: Exception indicating that the requested feature ID has not been found in
                                          the internal configuration of the SDK. This is usually normal and means that
                                          the feature flag has not yet been activated on Kameleoon's side
                                          (but code implementing the feature is already deployed on the
                                          web-application's side).
            VisitorCodeInvalid: Raise when the provided visitor code is not valid
                                 (empty, or longer than 255 characters)
            FeatureEnvironmentDisabled: Exception indicating that feature flag is disabled for the
                                        visitor's current environment.
        """
        (_, variation_key) = self.__get_feature_variation_key(visitor_code, feature_key)
        return variation_key

    def get_feature_variable(
        self, visitor_code: str, feature_key: str, variable_key: str
    ) -> Union[bool, str, float, Dict[str, Any], List[Any], None]:
        """
        Retrieves a feature variable value from assigned for visitor variation
        A feature variable can be changed easily via our web application.

        :param visitor_code: unique identifier of a visitor
        :type visitor_code: str
        :param feature_key: unique identifier of feature flag
        :type feature_key: str
        :param variable_name: variable name you want to retrieve
        :type variable_name: str

        :return: Feature variable value from assigned for visitor variation
        :rtype: Union[bool, str, float, Dict, List]

        :raises:
            FeatureNotFound: Exception indicating that the requested feature ID has not been found in
                                          the internal configuration of the SDK. This is usually normal and means that
                                          the feature flag has not yet been activated on Kameleoon's side
                                          (but code implementing the feature is already deployed on the
                                          web-application's side).
            FeatureVariableNotFound: Variable provided name doesn't exist in this feature
            VisitorCodeInvalid: Raise when the provided visitor code is not valid
                                 (empty, or longer than 255 characters)
            FeatureEnvironmentDisabled: Exception indicating that feature flag is disabled for the
                                        visitor's current environment.
        """

        (feature_flag, variation_key) = self.__get_feature_variation_key(visitor_code, feature_key)
        variation = feature_flag.get_variation(variation_key)
        variable = variation.get_variable_by_key(variable_key) if variation else None
        if variable is None:
            raise FeatureVariableNotFound(variable_key)
        return variable.get_value()

    ###
    #   Private API methods
    ###

    # Useless without storage
    # def __is_valid_saved_variation(
    #     self, visitor_code: str, experiment_id: int, respool_times: Dict[str, int]
    # ) -> Optional[int]:
    #     # get saved variation
    #     saved_variation_id = self.variation_storage.get_variation_id(
    #         visitor_code, experiment_id
    #     )
    #     if saved_variation_id is not None:
    #         # get respool time for saved variation id
    #         respool_time = respool_times.get(str(saved_variation_id))
    #         # checking variation for validity along with respoolTime
    #         return self.variation_storage.is_variation_id_valid(
    #             visitor_code, experiment_id, respool_time
    #         )
    #     return None

    # pylint: disable=W0238
    def __check_targeting(self, visitor_code: str, campaign: Dict[str, Any]):
        if (SEGMENT not in campaign) or (campaign[SEGMENT] is None):
            return True
        visitor = self._visitor_manager.get_visitor(visitor_code)
        campaign_id = campaign["id"]
        return campaign[SEGMENT].check_tree(
            lambda type: self.__get_condition_data(type, visitor, visitor_code, campaign_id)
        )

    def __check_targeting_id_object(self, visitor_code: str, campaign_id: int, targeting_object: Rule) -> bool:
        if targeting_object.targeting_segment is None:
            return True
        visitor = self._visitor_manager.get_visitor(visitor_code)
        return (
            targeting_object.targeting_segment.check_tree(
                lambda type: self.__get_condition_data(type, visitor, visitor_code, campaign_id)
            )
            is True
        )

    # pylint: disable=R0911
    @staticmethod
    def __get_condition_data(
        condition_type_literal: str, visitor: Optional[Visitor], visitor_code: str, campaign_id: int
    ):
        # pylint: disable=E1101,W0212
        condition_type = enum_from_literal(
            condition_type_literal, TargetingConditionType, TargetingConditionType.UNKNOWN
        )
        if visitor:
            if condition_type == TargetingConditionType.BROWSER:
                return visitor.browser
            if condition_type == TargetingConditionType.DEVICE_TYPE:
                return visitor.device
            if condition_type == TargetingConditionType.CUSTOM_DATUM:
                return visitor.custom_data
            if condition_type == TargetingConditionType.CONVERSIONS:
                return visitor.conversions
            if condition_type in (TargetingConditionType.PAGE_URL, TargetingConditionType.PAGE_TITLE):
                return visitor.page_view_visits
            if condition_type == TargetingConditionType.TARGET_EXPERIMENT:
                return visitor.variations
            if condition_type == TargetingConditionType.EXCLUSIVE_EXPERIMENT:
                return campaign_id, visitor.variations
        if condition_type == TargetingConditionType.VISITOR_CODE:
            return visitor_code
        if condition_type == TargetingConditionType.SDK_LANGUAGE:
            return SdkLanguageCondition.SdkInfo(SdkVersion.NAME, SdkVersion.VERSION)
        return None

    # pylint: disable=W0105
    """
    def _parse_json(self, custom_json: Dict[str, Any]):
        if custom_json["type"] == "Boolean":
            return bool(custom_json["value"])
        if custom_json["type"] == "String":
            return str(custom_json["value"])
        if custom_json["type"] == "Number":
            return float(custom_json["value"])
        if custom_json["type"] == "JSON":
            return json.loads(custom_json["value"])
        raise TypeError("Unknown type for feature variable")
    """

    def _init_fetch_configuration(self) -> None:
        """
        :return:
        """

        def initial_fetch():
            success = self._fetch_configuration()
            self._threading_readiness.set(success)
            self._async_readiness.dispose_on_set()

        run_in_thread(initial_fetch, with_event_loop=True)

    def _fetch_configuration(self, time_stamp: Optional[int] = None) -> bool:
        """
        Fetches configuration from CDN service.
        Should be run in a separate thead.
        :return: True if succeeds, otherwise - False.
        :rtype: bool
        """
        # pylint: disable=W0703
        success = False
        try:
            configuration_json = self._obtain_configuration(time_stamp)
            if configuration_json:
                self._data_file = DataFile.from_json(self._config.environment, configuration_json)
                self._cookie_manager.consent_required = (
                    self._data_file.settings.is_consent_required and not self._data_file.has_any_targeted_delivery_rule
                )
                self._network_manager.url_provider.apply_data_api_domain(self._data_file.settings.data_api_domain)
                self._call_update_handler_if_needed(time_stamp is not None)
            success = True
        except Exception as ex:
            self._config.logger.error(ex)
        self._manage_configuration_update(self._data_file.settings.real_time_update)
        return success

    def _call_update_handler_if_needed(self, need_call: bool) -> None:
        """
        Call the handler when configuraiton was updated with new time stamp
        :param need_call: this parameters indicates if we need to call handler or not
        :type need_call: bool
        :return:  None
        """
        if need_call and self._update_configuration_handler is not None:
            self._update_configuration_handler()

    def _manage_configuration_update(self, is_real_time_update: bool):
        if is_real_time_update:
            if self._real_time_configuration_service is None:
                url = self._network_manager.url_provider.make_real_time_url()
                self._real_time_configuration_service = RealTimeConfigurationService(
                    url,
                    lambda real_time_event: self._fetch_configuration(real_time_event.time_stamp),
                    logger=self._config.logger,
                )
        else:
            if self._real_time_configuration_service is not None:
                self._real_time_configuration_service.close()
                self._real_time_configuration_service = None

    def get_engine_tracking_code(self, visitor_code: str) -> str:
        """
        The `get_engine_tracking_code` returns the JavaScript code to be inserted in your page
        to send automatically the exposure events to the analytics solution you are using.
        :param visitor_code: Unique identifier of the user. This field is mandatory.
        :type visitor_code: str
        :return: Tracking code
        :rtype: str
        """
        visitor = self._visitor_manager.get_visitor(visitor_code)
        visitor_variations = visitor.variations if visitor else None
        return self._hybrid_manager.get_engine_tracking_code(visitor_variations)

    def on_update_configuration(self, handler: Callable[[], None]):
        """
        The `on_update_configuration()` method allows you to handle the event when configuration
        has updated data. It takes one input parameter: callable **handler**. The handler
        that will be called when the configuration is updated using a real-time configuration event.
        :param handler: The handler that will be called when the configuration
        is updated using a real-time configuration event.
        :type need_call: Callable[[None], None]
        :return:  None
        """
        self._update_configuration_handler = handler

    def __add_fetch_configuration_job(self) -> None:
        """
        Add job for updating configuration with specific interval (polling mode)
        :return: None
        """
        self._scheduler.schedule_job(
            "Client._fetch_configuration_job",
            self._config.refresh_interval_second,
            self._fetch_configuration_job,
        )

    def _fetch_configuration_job(self) -> None:
        if not self._data_file.settings.real_time_update:
            self._fetch_configuration()

    def _clear_timer(self) -> None:
        """
        Remove timer which updates configuration with specific interval (polling mode)
        :return: None
        """
        try:
            if self._timer:
                self._timer.cancel()
                self._timer = None
        except AttributeError:
            pass

    def _obtain_configuration(self, time_stamp: Optional[int]) -> Optional[Dict[str, Any]]:
        """
        Obtaining configuration from CDN service.
        Should be run in a separate thead.
        :param sitecode:
        :type: str
        :return: None
        """
        self._config.logger.debug("Obtaining configuration")
        service: ConfigurationService = self._network_manager.get_service(ConfigurationService)
        response_coro = service.fetch_configuration(self._config.environment, time_stamp)
        try:
            loop = asyncio.get_event_loop()
        except Exception:  # pylint: disable=W0703
            loop = asyncio.new_event_loop()
        response = loop.run_until_complete(response_coro)
        if response.code and (response.code // 100 == 2):
            return response.content
        return None

    def __make_sync_call_anyway(self, coro: Coroutine[Any, Any, Any], method_name: str) -> Optional[Any]:
        try:
            asyncio.get_running_loop()
            self._config.logger.warning(
                f"Called synchronous `{method_name}` method from asynchronous code. "
                f"Please use `{method_name}_async` method instead."
            )
        except Exception:  # pylint: disable=W0703
            result = get_loop().run_until_complete(coro)
            return result
        if self._thread_event_loop is None:
            self._thread_event_loop = ThreadEventLoop()
            self._thread_event_loop.start()
            self._config.logger.warning(
                "Despite the mono-thread mode an event loop background thread has "
                f"been started because of the call of synchronous `{method_name}` method"
            )
        future = self._thread_event_loop.run_coro(coro)
        while not future.done():
            time.sleep(0.01)
        if future.cancelled():
            self._config.logger.error("`%s` call was cancelled", method_name)
        elif future.exception():
            self._config.logger.error("`%s` call failed with exception: %s", method_name, future.exception())
        else:
            return future.result()
        return None

    def __run_call(self, coro: Coroutine[Any, None, Any]):
        try:
            if self._config.multi_threading:
                cast(ThreadEventLoop, self._thread_event_loop).run_coro(coro)
            else:
                invoke_coro(coro)
        except Exception as ex:  # pylint: disable=W0703
            self._config.logger.error("Exception occurred during call run: %s", ex)

    def __is_sync_mode(self) -> bool:
        if self._config.multi_threading:
            return False
        return not has_running_event_loop()

    def __send_tracking_request(self, visitor_code: str, visitor: Optional[Visitor], force_request=True) -> None:
        if (visitor is None) and self._data_file.settings.is_consent_required:
            return
        if visitor:
            consent = not self._data_file.settings.is_consent_required or visitor.legal_consent
            user_agent = visitor.user_agent
            unsent = self.__select_unsent_data(visitor, consent)
        else:
            consent = True
            user_agent = None
            unsent = []
        if len(unsent) == 0:
            if not (force_request and consent):
                return
            unsent.append(ActivityEvent())
        service: DataService = self._network_manager.get_service(DataService)
        coro = service.send_tracking_data(visitor_code, unsent, user_agent, sync=self.__is_sync_mode())

        async def call() -> Response:
            response = await coro
            if response.success:
                for sendable_data in unsent:
                    sendable_data.mark_as_sent()
            return response

        self.__run_call(call())

    @staticmethod
    def __select_unsent_data(visitor: Visitor, consent: bool) -> List[Sendable]:
        if consent:
            return [sd for sd in visitor.enumerate_sendable_data() if not sd.sent]
        tdr_variations = (av for av in visitor.variations.values() if av.rule_type == RuleType.TARGETED_DELIVERY)
        return [sd for sd in itertools.chain(visitor.conversions, tdr_variations) if not sd.sent]

    def __get_feature_variation_key(self, visitor_code: str, feature_key: str) -> Tuple[FeatureFlag, str]:
        """
        helper method for getting variation key for feature flag
        """
        validate_visitor_code(visitor_code)
        feature_flag = self._data_file.get_feature_flag(feature_key)
        (variation, rule) = self.__calculate_variation_rule_for_feature(visitor_code, feature_flag)
        variation_key = self.__calculate_variation_key(variation, rule, feature_flag)
        visitor = self.__assign_feature_variation(visitor_code, rule, variation)
        self.__send_tracking_request(visitor_code, visitor)
        return (feature_flag, variation_key)

    def __assign_feature_variation(
        self, visitor_code: str, rule: Optional[Rule], variation: Optional[VariationByExposition]
    ) -> Optional[Visitor]:
        visitor = self._visitor_manager.get_visitor(visitor_code)
        if rule and variation and (variation.variation_id is not None):
            if visitor is None:
                visitor = self._visitor_manager.get_or_create_visitor(visitor_code)
            as_variation = AssignedVariation(rule.experiment_id, variation.variation_id, rule.type)
            visitor.assign_variation(as_variation)
        return visitor

    def __calculate_variation_rule_for_feature(
        self, visitor_code: str, feature_flag: FeatureFlag
    ) -> Tuple[Optional[VariationByExposition], Optional[Rule]]:
        """helper method for calculate variation key for feature flag"""
        for rule in feature_flag.rules:
            # check if visitor is targeted for rule, else next rule
            if not self.__check_targeting_id_object(visitor_code, feature_flag.id_, rule):
                continue
            # uses for rule exposition
            hash_rule = obtain_hash_double_rule(visitor_code, rule.id_, rule.respool_time)
            # check main expostion for rule with hashRule
            if hash_rule <= rule.exposition:
                if rule.is_targeted_delivery and len(rule.variation_by_exposition) > 0:
                    return (rule.variation_by_exposition[0], rule)

                # uses for variation's expositions
                hash_variation = obtain_hash_double_rule(visitor_code, rule.experiment_id, rule.respool_time)
                # get variation with hash_variation
                variation = rule.get_variation(hash_variation)
                if variation:
                    return (variation, rule)
            elif rule.is_targeted_delivery:
                break
        return (None, None)

    @staticmethod
    def __calculate_variation_key(
        var_by_exp: Optional[VariationByExposition],
        rule: Optional[Rule],
        feature_flag: FeatureFlag,
    ) -> str:
        if var_by_exp:
            return var_by_exp.variation_key
        if rule and rule.is_experimentation:
            return Variation.Type.OFF.value
        return feature_flag.default_variation_key

    def _is_consent_given(self, visitor_code: str) -> bool:
        return (not self._data_file.settings.is_consent_required) or (
            (visitor := self._visitor_manager.get_visitor(visitor_code)) is not None and visitor.legal_consent
        )
