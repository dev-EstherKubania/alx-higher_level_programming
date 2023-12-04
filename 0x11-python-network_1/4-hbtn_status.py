#!/usr/bin/python3
"""
Fetches the content of https://alx-intranet.hbtn.io/status using requests.
Displays the body of the response in a specific format.

Requirements:
- You must use the package requests.
- You are not allowed to import packages other than requests.
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
