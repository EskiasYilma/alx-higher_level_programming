#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -X OPTIONS "$1" | awk -F': ' '/^allow:/ {print $2}'
