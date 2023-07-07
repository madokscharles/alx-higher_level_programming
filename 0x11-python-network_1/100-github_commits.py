#!/usr/bin/python3
"""
Script takes 2 arguments
Lists 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            argv[2], argv[1])

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
