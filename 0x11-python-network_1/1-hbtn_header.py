#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL\
 and displays the value of the X-Request-Id variable found\
  in the header of the response.
"""
import urllib.request
import sys


with urllib.request.urlopen(str(sys.argv[1])) as u:
    print(u.headers['X-Request-Id'])
