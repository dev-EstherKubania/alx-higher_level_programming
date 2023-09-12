#!/usr/bin/python3
"""
    class_to_json()
"""


def class_to_json(obj):
    """
        it returns the dictionary description with a simple data structure.
    """
    return obj.__dict__
