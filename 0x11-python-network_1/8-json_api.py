#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data)

    try:
        res_json = response.json()
        if res_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_json.get("id"), res_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
