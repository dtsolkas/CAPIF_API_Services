# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from api_invocation_logs.models.interface_description import InterfaceDescription
from api_invocation_logs.models.operation import Operation
from api_invocation_logs.models.protocol import Protocol


class Log(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Log - a model defined in OpenAPI

        api_id: The api_id of this Log.
        api_name: The api_name of this Log.
        api_version: The api_version of this Log.
        resource_name: The resource_name of this Log.
        uri: The uri of this Log [Optional].
        protocol: The protocol of this Log.
        operation: The operation of this Log [Optional].
        result: The result of this Log.
        invocation_time: The invocation_time of this Log [Optional].
        invocation_latency: The invocation_latency of this Log [Optional].
        input_parameters: The input_parameters of this Log [Optional].
        output_parameters: The output_parameters of this Log [Optional].
        src_interface: The src_interface of this Log [Optional].
        dest_interface: The dest_interface of this Log [Optional].
        fwd_interface: The fwd_interface of this Log [Optional].
    """


    api_id: str
    api_name: str
    api_version: str
    resource_name: str
    uri: Optional[str] = None
    protocol: Protocol
    operation: Optional[Operation] = None
    result: str
    invocation_time: Optional[datetime] = None
    invocation_latency: Optional[int] = None
    input_parameters: Optional[List] = None
    output_parameters: Optional[List] = None
    src_interface: Optional[InterfaceDescription] = None
    dest_interface: Optional[InterfaceDescription] = None
    fwd_interface: Optional[str] = None

    @validator("invocation_latency")
    def invocation_latency_min(cls, value):
        assert value >= 0
        return value

Log.update_forward_refs()
