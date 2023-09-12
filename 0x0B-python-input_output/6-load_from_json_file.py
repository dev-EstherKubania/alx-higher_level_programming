#!/usr/bin/python3
"""
Module: 6-load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.
    Args:
        filename (str): The name of the JSON file.
    Returns:
        object: The Python object loaded from the file.
    """
    with open(filename, 'r') as json_file:
        my_obj = json.load(json_file)
        return my_obj
