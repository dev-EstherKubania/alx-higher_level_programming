#!/usr/bin/python3
"""
Sends a request to the specified URL and displays the body of the response.
Handles urllib.error.HTTPError exceptions and prints the error code.

Requirements:
- You must use the packages urllib and sys.
- You are not allowed to import packages other than urllib and sys.
- You must use the with statement.
"""

import urllib.request
import urllib.error
import sys


def display_response(url):
    """
    Sends a request to the specified URL and displays the body of the response.

    Args:
        url (str): The URL to send the request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Display the response or error code
    display_response(url)
