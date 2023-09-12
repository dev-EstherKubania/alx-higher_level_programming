#!/usr/bin/python3
"""
    10-student: Module for Student class with to_json method.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with a first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list): A list of attribute names to retrieve. If None,
            retrieve all attributes.
        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if /
                    hasattr(self, attr)}
        return self.__dict__
