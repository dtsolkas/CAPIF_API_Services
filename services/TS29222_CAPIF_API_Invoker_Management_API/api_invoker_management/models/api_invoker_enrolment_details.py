# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api_invoker_management.models.base_model_ import Model
from api_invoker_management import util

from api_invoker_management.models.onboarding_information import OnboardingInformation  # noqa: E501
from api_invoker_management.models.service_api_description import ServiceAPIDescription  # noqa: E501
from api_invoker_management.models.websock_notif_config import WebsockNotifConfig  # noqa: E501
import re  # noqa: E501


class APIInvokerEnrolmentDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, api_invoker_id=None, onboarding_information=None, notification_destination=None, request_test_notification=None, websock_notif_config=None, api_list=None, api_invoker_information=None, supported_features=None):  # noqa: E501
        """APIInvokerEnrolmentDetails - a model defined in OpenAPI

        :param api_invoker_id: The api_invoker_id of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type api_invoker_id: str
        :param onboarding_information: The onboarding_information of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type onboarding_information: OnboardingInformation
        :param notification_destination: The notification_destination of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type notification_destination: str
        :param request_test_notification: The request_test_notification of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type request_test_notification: bool
        :param websock_notif_config: The websock_notif_config of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type websock_notif_config: WebsockNotifConfig
        :param api_list: The api_list of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type api_list: List[ServiceAPIDescription]
        :param api_invoker_information: The api_invoker_information of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type api_invoker_information: str
        :param supported_features: The supported_features of this APIInvokerEnrolmentDetails.  # noqa: E501
        :type supported_features: str
        """
        self.openapi_types = {
            'api_invoker_id': str,
            'onboarding_information': OnboardingInformation,
            'notification_destination': str,
            'request_test_notification': bool,
            'websock_notif_config': WebsockNotifConfig,
            'api_list': List[ServiceAPIDescription],
            'api_invoker_information': str,
            'supported_features': str
        }

        self.attribute_map = {
            'api_invoker_id': 'apiInvokerId',
            'onboarding_information': 'onboardingInformation',
            'notification_destination': 'notificationDestination',
            'request_test_notification': 'requestTestNotification',
            'websock_notif_config': 'websockNotifConfig',
            'api_list': 'apiList',
            'api_invoker_information': 'apiInvokerInformation',
            'supported_features': 'supportedFeatures'
        }

        self._api_invoker_id = api_invoker_id
        self._onboarding_information = onboarding_information
        self._notification_destination = notification_destination
        self._request_test_notification = request_test_notification
        self._websock_notif_config = websock_notif_config
        self._api_list = api_list
        self._api_invoker_information = api_invoker_information
        self._supported_features = supported_features

    @classmethod
    def from_dict(cls, dikt) -> 'APIInvokerEnrolmentDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The APIInvokerEnrolmentDetails of this APIInvokerEnrolmentDetails.  # noqa: E501
        :rtype: APIInvokerEnrolmentDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_invoker_id(self):
        """Gets the api_invoker_id of this APIInvokerEnrolmentDetails.

        API invoker ID assigned by the CAPIF core function to the API invoker while on-boarding the API invoker. Shall not be present in the HTTP POST request from the API invoker to the CAPIF core function, to on-board itself. Shall be present in all other HTTP requests and responses.  # noqa: E501

        :return: The api_invoker_id of this APIInvokerEnrolmentDetails.
        :rtype: str
        """
        return self._api_invoker_id

    @api_invoker_id.setter
    def api_invoker_id(self, api_invoker_id):
        """Sets the api_invoker_id of this APIInvokerEnrolmentDetails.

        API invoker ID assigned by the CAPIF core function to the API invoker while on-boarding the API invoker. Shall not be present in the HTTP POST request from the API invoker to the CAPIF core function, to on-board itself. Shall be present in all other HTTP requests and responses.  # noqa: E501

        :param api_invoker_id: The api_invoker_id of this APIInvokerEnrolmentDetails.
        :type api_invoker_id: str
        """

        self._api_invoker_id = api_invoker_id

    @property
    def onboarding_information(self):
        """Gets the onboarding_information of this APIInvokerEnrolmentDetails.


        :return: The onboarding_information of this APIInvokerEnrolmentDetails.
        :rtype: OnboardingInformation
        """
        return self._onboarding_information

    @onboarding_information.setter
    def onboarding_information(self, onboarding_information):
        """Sets the onboarding_information of this APIInvokerEnrolmentDetails.


        :param onboarding_information: The onboarding_information of this APIInvokerEnrolmentDetails.
        :type onboarding_information: OnboardingInformation
        """
        if onboarding_information is None:
            raise ValueError("Invalid value for `onboarding_information`, must not be `None`")  # noqa: E501

        self._onboarding_information = onboarding_information

    @property
    def notification_destination(self):
        """Gets the notification_destination of this APIInvokerEnrolmentDetails.

        string providing an URI formatted according to IETF RFC 3986.  # noqa: E501

        :return: The notification_destination of this APIInvokerEnrolmentDetails.
        :rtype: str
        """
        return self._notification_destination

    @notification_destination.setter
    def notification_destination(self, notification_destination):
        """Sets the notification_destination of this APIInvokerEnrolmentDetails.

        string providing an URI formatted according to IETF RFC 3986.  # noqa: E501

        :param notification_destination: The notification_destination of this APIInvokerEnrolmentDetails.
        :type notification_destination: str
        """
        if notification_destination is None:
            raise ValueError("Invalid value for `notification_destination`, must not be `None`")  # noqa: E501

        self._notification_destination = notification_destination

    @property
    def request_test_notification(self):
        """Gets the request_test_notification of this APIInvokerEnrolmentDetails.

        Set to true by Subscriber to request the CAPIF core function to send a test notification as defined in in subclause 7.6. Set to false or omitted otherwise.  # noqa: E501

        :return: The request_test_notification of this APIInvokerEnrolmentDetails.
        :rtype: bool
        """
        return self._request_test_notification

    @request_test_notification.setter
    def request_test_notification(self, request_test_notification):
        """Sets the request_test_notification of this APIInvokerEnrolmentDetails.

        Set to true by Subscriber to request the CAPIF core function to send a test notification as defined in in subclause 7.6. Set to false or omitted otherwise.  # noqa: E501

        :param request_test_notification: The request_test_notification of this APIInvokerEnrolmentDetails.
        :type request_test_notification: bool
        """

        self._request_test_notification = request_test_notification

    @property
    def websock_notif_config(self):
        """Gets the websock_notif_config of this APIInvokerEnrolmentDetails.


        :return: The websock_notif_config of this APIInvokerEnrolmentDetails.
        :rtype: WebsockNotifConfig
        """
        return self._websock_notif_config

    @websock_notif_config.setter
    def websock_notif_config(self, websock_notif_config):
        """Sets the websock_notif_config of this APIInvokerEnrolmentDetails.


        :param websock_notif_config: The websock_notif_config of this APIInvokerEnrolmentDetails.
        :type websock_notif_config: WebsockNotifConfig
        """

        self._websock_notif_config = websock_notif_config

    @property
    def api_list(self):
        """Gets the api_list of this APIInvokerEnrolmentDetails.

        The list of service APIs that the API Invoker is allowed to invoke  # noqa: E501

        :return: The api_list of this APIInvokerEnrolmentDetails.
        :rtype: List[ServiceAPIDescription]
        """
        return self._api_list

    @api_list.setter
    def api_list(self, api_list):
        """Sets the api_list of this APIInvokerEnrolmentDetails.

        The list of service APIs that the API Invoker is allowed to invoke  # noqa: E501

        :param api_list: The api_list of this APIInvokerEnrolmentDetails.
        :type api_list: List[ServiceAPIDescription]
        """
        if api_list is not None and len(api_list) < 1:
            raise ValueError("Invalid value for `api_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._api_list = api_list

    @property
    def api_invoker_information(self):
        """Gets the api_invoker_information of this APIInvokerEnrolmentDetails.

        Generic information related to the API invoker such as details of the device or the application.  # noqa: E501

        :return: The api_invoker_information of this APIInvokerEnrolmentDetails.
        :rtype: str
        """
        return self._api_invoker_information

    @api_invoker_information.setter
    def api_invoker_information(self, api_invoker_information):
        """Sets the api_invoker_information of this APIInvokerEnrolmentDetails.

        Generic information related to the API invoker such as details of the device or the application.  # noqa: E501

        :param api_invoker_information: The api_invoker_information of this APIInvokerEnrolmentDetails.
        :type api_invoker_information: str
        """

        self._api_invoker_information = api_invoker_information

    @property
    def supported_features(self):
        """Gets the supported_features of this APIInvokerEnrolmentDetails.

        A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported  # noqa: E501

        :return: The supported_features of this APIInvokerEnrolmentDetails.
        :rtype: str
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this APIInvokerEnrolmentDetails.

        A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported  # noqa: E501

        :param supported_features: The supported_features of this APIInvokerEnrolmentDetails.
        :type supported_features: str
        """
        if supported_features is not None and not re.search(r'^[A-Fa-f0-9]*$', supported_features):  # noqa: E501
            raise ValueError("Invalid value for `supported_features`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supported_features = supported_features