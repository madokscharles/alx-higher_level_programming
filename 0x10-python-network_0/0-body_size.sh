#!/bin/bash
# Script takes in a URL, send a request to it and displays size of the body
curl -s "$1" | wc -c
