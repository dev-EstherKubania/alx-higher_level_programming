#!/usr/bin/python3
""" 2-square: class Square """


class Square:
    """
    class represents a square.
    Attributes:
        __size (int): The size of the square.
    Method:
        __init__ : Initializes a new Square instance with an optional size.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
