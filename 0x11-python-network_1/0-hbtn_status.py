#!/usr/bin/python3
"""
Fetches the content of https://alx-intranet.hbtn.io/status using urllib.
Displays the body of the response in different formats.
"""

import urllib.request


def fetch_status(url):
    """
    Fetches the content of the specified URL using urllib.

    Args:
        url (str): The URL to fetch.

    Returns:
        bytes: The body of the HTTP response.
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
    return body

def display_response_info(body):
    """
    Displays information about the body of the HTTP response.

    Args:
        body (bytes): The body of the HTTP response.
    """
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))

if __name__ == "__main__":
    
    url = 'https://alx-intranet.hbtn.io/status'

    response_body = fetch_status(url)

    display_response_info(response_body)
