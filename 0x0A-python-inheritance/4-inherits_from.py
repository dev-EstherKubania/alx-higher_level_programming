#!/usr/bin/python3
"""
    a function to check if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
