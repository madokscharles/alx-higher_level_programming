#!/usr/bin/python3
""" Python script that takes ina uRL, send a request and displays body """
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
