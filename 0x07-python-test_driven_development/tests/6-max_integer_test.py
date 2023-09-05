#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(list=[]):
    """A function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    the_result = list[0]
    i = 1
    while i < len(list):
        if list[i] > the_result:
            the_result = list[i]
        i += 1
    return the_result
