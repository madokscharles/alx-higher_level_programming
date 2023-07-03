#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL
displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.error
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as r:
            print(r.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
