#!/usr/bin/python3
""" A python script that takes 2 arguments in order to solve this challenge """
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])
    res = requests.get(url)
    data = res.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                data[i].get("sha"),
                data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
