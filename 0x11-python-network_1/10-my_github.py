#!/usr/bin/python3
"""
Uses GitHub credentials (username and password)
GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = argv[1]
    token = argv[2]

    headers = {'Authorization': 'token {}'.format(token)}
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
