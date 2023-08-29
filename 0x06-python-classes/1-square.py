#!/usr/bin/python3
"""
Module contains: class Square 
that defines a square by: (based on 0-square.py)
"""
class Square:
     """
    Square: This class represents a square.
    Attributes:
        __size (int): The size of the square.
    Method:
        __init__(self, size): Initializes a new Square instance.
    """
    def __init__(self, size):
         """
        Initializes a new Square instance.
        Args:
            size (no type): The size of the square.
        """
        self.__size = size
