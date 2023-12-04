#!/usr/bin/python3
"""
Sends a request to the specified URL and displays the value of the X-Request
in the response header.

Requirements:
- You must use the packages requests and sys.
- You are not allowed to import packages other than requests and sys.
- The value of the X-Request-Id variable is different for each request.
"""

import requests
import sys


if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a request to the URL
    response = requests.get(url)

    # Get and display the value of the X-Request-Id variable
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
