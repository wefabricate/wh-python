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





class HeatPumpType(int, Enum):
    """
    LEGACY TYPE, Obsolete please do not use HeatPumpType, new properties split up into HeatPumpModel, DhwType and BoilerType
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3

    @classmethod
    def from_json(cls, json_str: str) -> HeatPumpType:
        """Create an instance of HeatPumpType from a JSON string"""
        return HeatPumpType(json.loads(json_str))

