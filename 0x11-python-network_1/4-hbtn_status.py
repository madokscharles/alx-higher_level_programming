#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    content = response.content.decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
