#!/usr/bin/python3
"""
Sends a POST request to the specified URL with the email as a parameter
and displays the body of the response (decoded in utf-8).

Requirements:
- You must use the packages urllib and sys.
- You are not allowed to import packages other than urllib and sys.
- The email must be sent in the email variable.
- You must use the with statement.
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include as a parameter.

    Returns:
        bytes: The body of the HTTP response.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
    return body


if __name__ == "__main__":
    # Check if a URL and email are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send a POST request with the email parameter
    response_body = post_email(url, email)

    # Decode and display the body of the response
    print(response_body.decode('utf-8'))
