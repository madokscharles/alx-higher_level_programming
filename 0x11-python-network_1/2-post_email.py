#!/usr/bin/python3
"""
Script takes in a URL and an email,
Sends a POST request to the passed URL with the email as a parameter.
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    email = {"email": argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(argv[1], data)
    with  urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
