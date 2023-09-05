#!/usr/bin/python3
""" say my name function """


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>."

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    
    # Print the message with the names
    print("My name is {} {}".format(first_name, last_name))
