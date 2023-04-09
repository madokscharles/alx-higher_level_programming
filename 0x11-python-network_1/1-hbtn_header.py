#!/usr/bin/python3
""" Python script takes in a URL, sends a request to the URL """

from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))
