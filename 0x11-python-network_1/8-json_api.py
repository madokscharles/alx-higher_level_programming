#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data)

    try:
        response_json = response.json()
    except ValueError:
        print("Not a valid JSON")
    if len(response_json) < 1 or ("id" and "name") not in response_json:
        print("No result")
    else:
        print("[{}] {}".format(response_json["id"], response_json["name"]))
