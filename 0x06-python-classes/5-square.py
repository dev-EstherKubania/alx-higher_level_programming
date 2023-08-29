#!/usr/bin/python3
""" Module 5-square """


class Square:
    """
        This class represents a square.
        Attributes:
            __size (int): The size of the square.
        Method:
            __init__ : Initializes a new Square instance with an optional size.
            area(self): Returns the current square area.
            size(self): Getter method to retrieve the size attribute.
            size(self, value): Setter method to set the size attribute.
    """
    def __init__(self, size=0):
        """
            Initializes a new Square instance with an optional size.
            Args:
                size (int): The size of the square (default is 0).
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.__size = size

    def area(self):
        """
            Returns the current square area.
            Returns:
                int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
            Getter method to retrieve the size attribute.
            Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
            Print the square using '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
