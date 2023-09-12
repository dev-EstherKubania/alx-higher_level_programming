#!/usr/bin/python3
"""
Module: 3-to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: The object to be converted to a JSON string.
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
