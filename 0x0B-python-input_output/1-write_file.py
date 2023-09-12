#!/usr/bin/python3
"""
Module: 1-write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the
    number of characters written.
    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.
    Note:
        If no filename is provided, an empty string is assumed.
        If no text is provided, an empty string is assumed.
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
