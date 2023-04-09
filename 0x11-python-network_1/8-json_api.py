#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        data_q = argv[1]
    else:
        data_q = ""

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'data_q': data_q})

    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
