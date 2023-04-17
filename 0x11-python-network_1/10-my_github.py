#!/usr/bin/python3
""" Script takes a Github credentials and uses GitHub API to display id """
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
