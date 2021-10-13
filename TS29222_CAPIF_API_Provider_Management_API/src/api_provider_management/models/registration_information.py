# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class RegistrationInformation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RegistrationInformation - a model defined in OpenAPI

        api_prov_pub_key: The api_prov_pub_key of this RegistrationInformation.
        api_prov_cert: The api_prov_cert of this RegistrationInformation [Optional].
    """

    api_prov_pub_key: str
    api_prov_cert: Optional[str] = None

RegistrationInformation.update_forward_refs()
