#!/usr/bin/python3
"""
    contains class Square
"""
from models.rectangle impiort Rectangle


class Square(Rectangle):
    """
        Square extends Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes Square (overrides Rectangle init)

            Args:
                size (int): Size of the square.
                x (int): x-coordinate of the square's position. Default is 0.
                y (int): y-coordinate of the square's position. Default is 0.
                id (int): Unique identifier for the square. Default is None.

            Returns:
                None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Returns the size of the square

            Returns:
                int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Sets the value of size

            Args:
                value (int): New size value.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than or equal to 0.

            Returns:
                None
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Assigns key/value arguments to attributes
            kwargs is skipped if args is not empty

            Args:
                *args - variable number of no-keyword args
                **kwargs - variable number of keyworded args

            Returns:
                None
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            Overloads str function

            Returns:
                str: Formatted string representing the Square instance.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square

            Returns:
                dict: Dictionary containing id, size, x, y.
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
