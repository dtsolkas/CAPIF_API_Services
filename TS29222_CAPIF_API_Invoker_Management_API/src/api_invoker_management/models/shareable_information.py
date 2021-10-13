# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ShareableInformation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ShareableInformation - a model defined in OpenAPI

        is_shareable: The is_shareable of this ShareableInformation.
        capif_prov_doms: The capif_prov_doms of this ShareableInformation [Optional].
    """

    is_shareable: bool
    capif_prov_doms: Optional[List[str]] = None

ShareableInformation.update_forward_refs()
