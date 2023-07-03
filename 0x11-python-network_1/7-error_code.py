#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL
displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    code = r.status_code

    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
