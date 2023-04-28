#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as u:
    x = u.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(x), x, x.decode('utf-8')))
