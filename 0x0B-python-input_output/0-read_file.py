#!/usr/bin/python3
"""
Module: 0-read_file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): The name of the file to be read.
    Note:
        If no filename is provided, an empty string is assumed.
    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
