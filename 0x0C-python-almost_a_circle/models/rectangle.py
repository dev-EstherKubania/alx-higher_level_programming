#!/usr/bin/python3
"""
    class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from Base.

    Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
    x (int): x-coordinate of the rectangle's position.
    y (int): y-coordinate of the rectangle's position.
    id (int): Unique identifier for the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): x-coordinate of the rectangle's position. Default is 0.
        y (int, optional): y-coordinate of the rectangle's position. Default is 0.
        id (int, optional): Unique identifier for the rectangle. Default is None.

        Returns:
        None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
        value (int): New width value.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
        value (int): New height value.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
        int: x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
        value (int): New x-coordinate value.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
        int: y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
        value (int): New y-coordinate value.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with '#' characters.

        Returns:
        None
        """
        for i in range(self.__height):
            print("#" * self.__width)
