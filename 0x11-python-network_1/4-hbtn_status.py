#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(r.content), r.content))
