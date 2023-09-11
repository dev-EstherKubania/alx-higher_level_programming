#!/usr/bin/python3
"""
    class Square from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square  inherits from class Rectangle
        Attributes:
            size (int): side of the square
        Methods:
            __init__ - initialises the square
    """
    def __init__(self, size):
        """
            initialises a Square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            Returns the area of the square
        """
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle",
                                    self.__size, self.__size))
