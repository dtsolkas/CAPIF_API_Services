# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from capif_events.models.routing_rule import RoutingRule


class TopologyHiding(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TopologyHiding - a model defined in OpenAPI

        api_id: The api_id of this TopologyHiding.
        routing_rules: The routing_rules of this TopologyHiding.
    """

    api_id: str
    routing_rules: List[RoutingRule]

TopologyHiding.update_forward_refs()
