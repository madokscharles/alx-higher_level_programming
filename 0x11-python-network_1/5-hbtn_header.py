#!/usr/bin/python3
""" Script takes in a URL, sends a request to it and displays value """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1]).headers.get("X-Request-Id")
    print(r)
