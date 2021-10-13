# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from capif_security.models.security_information import SecurityInformation
from capif_security.models.websock_notif_config import WebsockNotifConfig


class ServiceSecurity(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceSecurity - a model defined in OpenAPI

        security_info: The security_info of this ServiceSecurity.
        notification_destination: The notification_destination of this ServiceSecurity.
        request_test_notification: The request_test_notification of this ServiceSecurity [Optional].
        websock_notif_config: The websock_notif_config of this ServiceSecurity [Optional].
        supported_features: The supported_features of this ServiceSecurity [Optional].
    """

    security_info: List[SecurityInformation]
    notification_destination: str
    request_test_notification: Optional[bool] = None
    websock_notif_config: Optional[WebsockNotifConfig] = None
    supported_features: Optional[str] = None

    @validator("supported_features")
    def supported_features_pattern(cls, value):
        assert value is not None and re.match(r"^[A-Fa-f0-9]*$", value)
        return value

ServiceSecurity.update_forward_refs()
