#!/usr/bin/python3
""" Python script that takes ina URL and an email """
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {"email": argv[2]}
    data = urllib.parse.urlencode(email)

    with urllib.request.urlopen(url, data.encode()) as f:
        body = f.read().decode('utf-8')
        print(body)
