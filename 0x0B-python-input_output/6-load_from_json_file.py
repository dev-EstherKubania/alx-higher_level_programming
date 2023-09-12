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
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
