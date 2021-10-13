# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from api_provider_management.models.api_provider_func_role import ApiProviderFuncRole
from api_provider_management.models.registration_information import RegistrationInformation


class APIProviderFunctionDetails(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    APIProviderFunctionDetails - a model defined in OpenAPI

        api_prov_func_id: The api_prov_func_id of this APIProviderFunctionDetails [Optional].
        reg_info: The reg_info of this APIProviderFunctionDetails.
        api_prov_func_role: The api_prov_func_role of this APIProviderFunctionDetails.
        api_prov_func_info: The api_prov_func_info of this APIProviderFunctionDetails [Optional].
    """

    api_prov_func_id: Optional[str] = None
    reg_info: RegistrationInformation
    api_prov_func_role: ApiProviderFuncRole
    api_prov_func_info: Optional[str] = None

APIProviderFunctionDetails.update_forward_refs()
