#!/bin/bash
# Script takes in a URL, sends a request to it and displays the size in bytes
curl --silent "$1" | wc -c
