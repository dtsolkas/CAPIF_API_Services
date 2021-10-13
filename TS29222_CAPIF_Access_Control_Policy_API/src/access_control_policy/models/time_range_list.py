# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class TimeRangeList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TimeRangeList - a model defined in OpenAPI

        start_time: The start_time of this TimeRangeList [Optional].
        stop_time: The stop_time of this TimeRangeList [Optional].
    """

    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None

TimeRangeList.update_forward_refs()
