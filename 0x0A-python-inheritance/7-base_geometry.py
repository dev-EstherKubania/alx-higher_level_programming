#!/usr/bin/python3
"""
    class BaseGeometry
"""


class BaseGeometry:
    """
    A class representing basic geometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value, raising exceptions if it doesn't meet the criteria.
        - name: A string representing the name of the value.
        - value: The value to be validated.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
