#!/usr/bin/python3
"""
Module: 2-append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the
    number of characters added.
    Args:
        filename (str): The name of the file to be written or appended.
        text (str): The string to be appended to the file.
    Note:
        If no filename is provided, an empty string is assumed.
        If no text is provided, an empty string is assumed.
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
