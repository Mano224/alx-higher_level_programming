#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests

response = requests.get("https://alx-intranet.hbtn.io/status")


print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
