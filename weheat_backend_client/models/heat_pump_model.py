# coding: utf-8

"""
    Weheat Backend

    This is the backend for the Weheat project

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class HeatPumpModel(int, Enum):
    """
    Model of the heat pump   - BlackBirdP80: BlackBird P80 heat pump (0)   - BlackBirdP60: BlackBird P60 heat pump (1)   - SparrowP60: Sparrow P60 heat pump (2)
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2

    @classmethod
    def from_json(cls, json_str: str) -> HeatPumpModel:
        """Create an instance of HeatPumpModel from a JSON string"""
        return HeatPumpModel(json.loads(json_str))


