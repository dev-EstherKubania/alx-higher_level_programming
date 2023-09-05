#!/usr/bin/python3
"""
This module defines a class Rectangle that represents a rectangle shape.
Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


class Rectangle:
    """
    The Rectangle class defines a rectangle object.
    Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Args:
            value (int): The new width value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Args:
            value (int): The new height value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

