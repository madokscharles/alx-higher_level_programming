#!/usr/bin/python3
"""
Script takes 2 arguments
Lists 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == '__main__':
    try:
        repo = argv[1]
        owner = argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(
                owner, repo)

        response = requests.get(url)
        commits = response.json()

        for i in range(0, 10):
            print('{}: {}'.format(commits[i]['sha'],
                                  commits[i]['commit']['author']['name']))
    except Exception:
        pass
