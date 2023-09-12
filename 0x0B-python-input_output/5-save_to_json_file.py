#!/usr/bin/python3
"""
Module: 5-save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a JSON file.
    Args:
        my_obj (object): The Python object to be saved to the file.
        filename (str): The name of the file to save the JSON
        representation to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
