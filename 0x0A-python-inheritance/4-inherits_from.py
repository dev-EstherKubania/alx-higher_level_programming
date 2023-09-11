#!/usr/bin/python3
"""
    a function to check if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class)
