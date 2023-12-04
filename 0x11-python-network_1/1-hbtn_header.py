#!/usr/bin/python3
"""
Sends a request to the specified URL and displays the variable
found in the header of the response.

Requirements:
- You must use the packages urllib and sys.
- You are not allowed to import packages other than urllib and sys.
- The value of the X-Request-Id variable is different for each request.
- You must use a with statement.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get('X-Request-Id')
    return x_request_id


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    x_request_id_value = fetch_x_request_id(url)

    print(x_request_id_value)
