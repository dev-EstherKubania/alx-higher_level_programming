#!/usr/bin/python3
"""
    text_indentation()
"""


def text_indentation(text):
    """
        text_indentation prints text with 2 new lines after . ? or :
        Args:
            text (str): text to be formatted
    """

    a_temp = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) is 0:
        return

    for letter in text:
        a_temp += letter
        if letter in ["?", ":", "."]:
            while a_temp[0] is " ":
                a_temp = a_temp[1:]
            print(a_temp)
            print()
            a_temp = ""
    if len(a_temp) != 0:
        try:
            while a_temp[0] is " ":
                a_temp = a_temp[1:]
        except:
            pass
        print(a_temp, end="")
