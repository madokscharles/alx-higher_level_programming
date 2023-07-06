#!/usr/bin/python3
"""
Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    arg_length = len(argv)

    if arg_length == 2:
        q = argv[1]
    else:
        q = ''
    response = requests.post(url, data={'q': q})
    try:
        response = response.json()
        if not response:
            print('No result')
        else:
            print('[{}] {}'.format(response['id'], response['name']))
    except ValueError:
        print('Not a valid JSON')
