#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and \
password) and uses the GitHub API to display your id.
"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json()['id'])
    except Exception:
        print("None")
