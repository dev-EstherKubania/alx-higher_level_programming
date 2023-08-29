#!/usr/bin/python3
""" Module 3-square """


class Square:
    """
        class represents a square.

        Attributes:
            __size (int): The size of the square.

        Methods:
            __init__: Initializes a new Square instance with an optional size.
            area(self): Returns the current square area.
    """
    def __init__(self, size=0):
        """
            Initializes a new Square instance with an optional size.
            Args:
            size (int): The size of the square.
            Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
