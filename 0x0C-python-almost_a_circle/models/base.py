#!/usr/bin/python3
"""
    contains a class Base.
"""


import json
import csv


class Base:
    """
    Base class for managing unique IDs.
    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of objects.
        id (int): Public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        Args:
            id (int, optional): The ID for the instance. If not provided, a unique ID will be generated.
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
