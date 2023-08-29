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
    def __init__(self, size=0, position=(0, 0)):
        """
            Initializes a new Square instance with an optional size.
            Args:
                size (int): The size of the square.
                position (tuple): The position of the square
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
            Getter method to retrieve the position attribute.
            Returns:
                tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Setter method to set the position attribute.
            Args:
                value (tuple): The new position of the square.
            Raises:
                TypeError: If position is not a tuple of 2 positive integers.
                ValueError: If position values are less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
            Print the square using '#' characters and respecting the position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
