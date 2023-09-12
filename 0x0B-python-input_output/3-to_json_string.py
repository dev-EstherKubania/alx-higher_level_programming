#!/usr/bin/python3
"""
Module: 3-to_json_string

This module provides a function to convert an object to its JSON representation.
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
