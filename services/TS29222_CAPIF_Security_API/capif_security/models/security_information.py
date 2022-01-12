# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from capif_security.models.base_model_ import Model
from capif_security.models.interface_description import InterfaceDescription
from capif_security.models.security_method import SecurityMethod
from capif_security import util

from capif_security.models.interface_description import InterfaceDescription  # noqa: E501
from capif_security.models.security_method import SecurityMethod  # noqa: E501

class SecurityInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interface_details=None, aef_id=None, pref_security_methods=None, sel_security_method=None, authentication_info=None, authorization_info=None):  # noqa: E501
        """SecurityInformation - a model defined in OpenAPI

        :param interface_details: The interface_details of this SecurityInformation.  # noqa: E501
        :type interface_details: InterfaceDescription
        :param aef_id: The aef_id of this SecurityInformation.  # noqa: E501
        :type aef_id: str
        :param pref_security_methods: The pref_security_methods of this SecurityInformation.  # noqa: E501
        :type pref_security_methods: List[SecurityMethod]
        :param sel_security_method: The sel_security_method of this SecurityInformation.  # noqa: E501
        :type sel_security_method: SecurityMethod
        :param authentication_info: The authentication_info of this SecurityInformation.  # noqa: E501
        :type authentication_info: str
        :param authorization_info: The authorization_info of this SecurityInformation.  # noqa: E501
        :type authorization_info: str
        """
        self.openapi_types = {
            'interface_details': InterfaceDescription,
            'aef_id': str,
            'pref_security_methods': List[SecurityMethod],
            'sel_security_method': SecurityMethod,
            'authentication_info': str,
            'authorization_info': str
        }

        self.attribute_map = {
            'interface_details': 'interfaceDetails',
            'aef_id': 'aefId',
            'pref_security_methods': 'prefSecurityMethods',
            'sel_security_method': 'selSecurityMethod',
            'authentication_info': 'authenticationInfo',
            'authorization_info': 'authorizationInfo'
        }

        self._interface_details = interface_details
        self._aef_id = aef_id
        self._pref_security_methods = pref_security_methods
        self._sel_security_method = sel_security_method
        self._authentication_info = authentication_info
        self._authorization_info = authorization_info

    @classmethod
    def from_dict(cls, dikt) -> 'SecurityInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SecurityInformation of this SecurityInformation.  # noqa: E501
        :rtype: SecurityInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface_details(self):
        """Gets the interface_details of this SecurityInformation.


        :return: The interface_details of this SecurityInformation.
        :rtype: InterfaceDescription
        """
        return self._interface_details

    @interface_details.setter
    def interface_details(self, interface_details):
        """Sets the interface_details of this SecurityInformation.


        :param interface_details: The interface_details of this SecurityInformation.
        :type interface_details: InterfaceDescription
        """

        self._interface_details = interface_details

    @property
    def aef_id(self):
        """Gets the aef_id of this SecurityInformation.

        Identifier of the API exposing function  # noqa: E501

        :return: The aef_id of this SecurityInformation.
        :rtype: str
        """
        return self._aef_id

    @aef_id.setter
    def aef_id(self, aef_id):
        """Sets the aef_id of this SecurityInformation.

        Identifier of the API exposing function  # noqa: E501

        :param aef_id: The aef_id of this SecurityInformation.
        :type aef_id: str
        """

        self._aef_id = aef_id

    @property
    def pref_security_methods(self):
        """Gets the pref_security_methods of this SecurityInformation.

        Security methods preferred by the API invoker for the API interface.  # noqa: E501

        :return: The pref_security_methods of this SecurityInformation.
        :rtype: List[SecurityMethod]
        """
        return self._pref_security_methods

    @pref_security_methods.setter
    def pref_security_methods(self, pref_security_methods):
        """Sets the pref_security_methods of this SecurityInformation.

        Security methods preferred by the API invoker for the API interface.  # noqa: E501

        :param pref_security_methods: The pref_security_methods of this SecurityInformation.
        :type pref_security_methods: List[SecurityMethod]
        """
        if pref_security_methods is None:
            raise ValueError("Invalid value for `pref_security_methods`, must not be `None`")  # noqa: E501
        if pref_security_methods is not None and len(pref_security_methods) < 1:
            raise ValueError("Invalid value for `pref_security_methods`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._pref_security_methods = pref_security_methods

    @property
    def sel_security_method(self):
        """Gets the sel_security_method of this SecurityInformation.


        :return: The sel_security_method of this SecurityInformation.
        :rtype: SecurityMethod
        """
        return self._sel_security_method

    @sel_security_method.setter
    def sel_security_method(self, sel_security_method):
        """Sets the sel_security_method of this SecurityInformation.


        :param sel_security_method: The sel_security_method of this SecurityInformation.
        :type sel_security_method: SecurityMethod
        """

        self._sel_security_method = sel_security_method

    @property
    def authentication_info(self):
        """Gets the authentication_info of this SecurityInformation.

        Authentication related information  # noqa: E501

        :return: The authentication_info of this SecurityInformation.
        :rtype: str
        """
        return self._authentication_info

    @authentication_info.setter
    def authentication_info(self, authentication_info):
        """Sets the authentication_info of this SecurityInformation.

        Authentication related information  # noqa: E501

        :param authentication_info: The authentication_info of this SecurityInformation.
        :type authentication_info: str
        """

        self._authentication_info = authentication_info

    @property
    def authorization_info(self):
        """Gets the authorization_info of this SecurityInformation.

        Authorization related information  # noqa: E501

        :return: The authorization_info of this SecurityInformation.
        :rtype: str
        """
        return self._authorization_info

    @authorization_info.setter
    def authorization_info(self, authorization_info):
        """Sets the authorization_info of this SecurityInformation.

        Authorization related information  # noqa: E501

        :param authorization_info: The authorization_info of this SecurityInformation.
        :type authorization_info: str
        """

        self._authorization_info = authorization_info