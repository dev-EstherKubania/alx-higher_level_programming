#!/usr/bin/python3
"""
    Module: 8-rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry.
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """
        validate and initiailize width and height
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectrangle. 
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
