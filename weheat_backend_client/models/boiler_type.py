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





class BoilerType(int, Enum):
    """
    Type of model and use of the heat pump   - Unknown: Not known if a boiler is in the installation (0)   - None: No boiler detected (1)   - OnOff: On/off boiler detected (2)   - OpenTherm: OpenTherm boiler detected (3)
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3

    @classmethod
    def from_json(cls, json_str: str) -> BoilerType:
        """Create an instance of BoilerType from a JSON string"""
        return BoilerType(json.loads(json_str))


