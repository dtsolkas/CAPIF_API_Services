# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from capif_events.models.aef_profile import AefProfile
from capif_events.models.published_api_path import PublishedApiPath
from capif_events.models.shareable_information import ShareableInformation


class ServiceAPIDescription(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceAPIDescription - a model defined in OpenAPI

        api_name: The api_name of this ServiceAPIDescription.
        api_id: The api_id of this ServiceAPIDescription [Optional].
        aef_profiles: The aef_profiles of this ServiceAPIDescription [Optional].
        description: The description of this ServiceAPIDescription [Optional].
        supported_features: The supported_features of this ServiceAPIDescription [Optional].
        shareable_info: The shareable_info of this ServiceAPIDescription [Optional].
        service_api_category: The service_api_category of this ServiceAPIDescription [Optional].
        api_supp_feats: The api_supp_feats of this ServiceAPIDescription [Optional].
        pub_api_path: The pub_api_path of this ServiceAPIDescription [Optional].
        ccf_id: The ccf_id of this ServiceAPIDescription [Optional].
    """

    api_name: str
    api_id: Optional[str] = None
    aef_profiles: Optional[List[AefProfile]] = None
    description: Optional[str] = None
    supported_features: Optional[str] = None
    shareable_info: Optional[ShareableInformation] = None
    service_api_category: Optional[str] = None
    api_supp_feats: Optional[str] = None
    pub_api_path: Optional[PublishedApiPath] = None
    ccf_id: Optional[str] = None

    @validator("supported_features")
    def supported_features_pattern(cls, value):
        assert value is not None and re.match(r"^[A-Fa-f0-9]*$", value)
        return value

    @validator("api_supp_feats")
    def api_supp_feats_pattern(cls, value):
        assert value is not None and re.match(r"^[A-Fa-f0-9]*$", value)
        return value

ServiceAPIDescription.update_forward_refs()
