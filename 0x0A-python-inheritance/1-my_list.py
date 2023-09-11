#!/usr/bin/python3
"""
    class MyList
"""


class MyList(list):
    """
        The class inherits from list.
        Methods:
            print_sorted- it prints the list in ascending order
    """
    def print_sorted(self):
        """
            it prints list in ascending order
        """
        print(sorted(self))
