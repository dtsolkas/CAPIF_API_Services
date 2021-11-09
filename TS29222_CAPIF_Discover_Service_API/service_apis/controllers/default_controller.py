import connexion
import six

from service_apis.models.communication_type import CommunicationType  # noqa: E501
from service_apis.models.data_format import DataFormat  # noqa: E501
from service_apis.models.discovered_apis import DiscoveredAPIs  # noqa: E501
from service_apis.models.problem_details import ProblemDetails  # noqa: E501
from service_apis.models.protocol import Protocol  # noqa: E501
from service_apis import util

from ..core import discoveredapis
import pymongo
import secrets
import json
from flask_jwt_extended import jwt_required


@jwt_required()
def all_service_apis_get(api_invoker_id, api_name=None, api_version=None, comm_type=None, protocol=None, aef_id=None, data_format=None, api_cat=None, supported_features=None, api_supported_features=None):  # noqa: E501
    """all_service_apis_get

    Discover published service APIs and retrieve a collection of APIs according to certain filter criteria. # noqa: E501

    :param api_invoker_id: String identifying the API invoker assigned by the CAPIF core function. It also represents the CCF identifier in the CAPIF-6/6e interface.
    :type api_invoker_id: str
    :param api_name: API name, it is set as {apiName} part of the URI structure as defined in subclause 4.4 of 3GPP TS 29.501.
    :type api_name: str
    :param api_version: API major version the URI (e.g. v1).
    :type api_version: str
    :param comm_type: Communication type used by the API (e.g. REQUEST_RESPONSE).
    :type comm_type: dict | bytes
    :param protocol: Protocol used by the API.
    :type protocol: dict | bytes
    :param aef_id: AEF identifer.
    :type aef_id: str
    :param data_format: Data formats used by the API (e.g. serialization protocol JSON used).
    :type data_format: dict | bytes
    :param api_cat: The service API category to which the service API belongs to.
    :type api_cat: str
    :param supported_features: Features supported by the NF consumer for the CAPIF Discover Service API.
    :type supported_features: str
    :param api_supported_features: Features supported by the discovered service API indicated by api-name parameter. This may only be present if api-name query parameter is present.
    :type api_supported_features: str

    :rtype: DiscoveredAPIs
    """

    discovered_apis = discoveredapis.get_discoveredapis(api_invoker_id, api_name, api_version, comm_type, protocol, aef_id, data_format, api_cat, supported_features, api_supported_features)
    response = discovered_apis, 200

    # if connexion.request.is_json:
    #     comm_type =  CommunicationType.from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     protocol =  Protocol.from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     data_format =  DataFormat.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    return response
