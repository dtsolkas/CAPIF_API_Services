# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from api_invoker_management.models.security_method import SecurityMethod


class InterfaceDescription(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InterfaceDescription - a model defined in OpenAPI

        ipv4_addr: The ipv4_addr of this InterfaceDescription [Optional].
        ipv6_addr: The ipv6_addr of this InterfaceDescription [Optional].
        port: The port of this InterfaceDescription [Optional].
        security_methods: The security_methods of this InterfaceDescription [Optional].
    """

    ipv4_addr: Optional[str] = None
    ipv6_addr: Optional[str] = None
    port: Optional[int] = None
    security_methods: Optional[List[SecurityMethod]] = None

    @validator("port")
    def port_max(cls, value):
        assert value <= 65535
        return value

    @validator("port")
    def port_min(cls, value):
        assert value >= 0
        return value

InterfaceDescription.update_forward_refs()
