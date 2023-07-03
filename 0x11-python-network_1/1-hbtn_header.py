#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response.
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
