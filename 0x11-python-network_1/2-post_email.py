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
    data = urllib.parse.urlencode(email)

    with urllib.request.urlopen(argv[1], data.encode()) as f:
        body = f.read().decode('utf-8')
        print(body)
