#!/bin/bash
# Bash script takes in a URL, sends a POST request to it and displays the body
curl -s -X POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' $1
