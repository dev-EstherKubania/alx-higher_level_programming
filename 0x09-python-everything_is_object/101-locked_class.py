#!/usr/bin/python3
"""
    101-locked_class: Class LockedClass
"""


class LockedClass:
    """
    A class that restricts instance attributes to only 'first_name'.

    Attributes:
        first_name (str): The first name attribute allowed for instance creation.
    """
    __slots__ = ['first_name']
