# coding: utf-8

"""
    Weheat Backend

    This is the backend for the Weheat project

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class HeatPumpModel(int, Enum):
    """
    Model of the heat pump   - BlackBirdP80: BlackBird P80 heat pump (0)   - BlackBirdP60: BlackBird P60 heat pump (1)   - SparrowP60Brown: Sparrow P60 heat pump, colour brown (default) (2)   - SparrowP60Green: Sparrow P60 heat pump, colour green (3)   - SparrowP60Grey: Sparrow P60 heat pump, colour grey (4)   - FlintP40: Flint P40 heat pump (5)
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3
    NUMBER_4 = 4
    NUMBER_5 = 5

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HeatPumpModel from a JSON string"""
        return cls(json.loads(json_str))


