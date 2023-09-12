#!/usr/bin/python3
"""
A python script that adds all arguments to a Python List.
"""

import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


if __name__ == "__main__":

    filename = "add_item.json"

    try:
        item_list = load_from_json_file(filename)
    except FileNotFoundError:
        item_list = []

    for item in sys.argv[1:]:
        item_list.append(item)

    save_to_json_file(item_list, filename)
