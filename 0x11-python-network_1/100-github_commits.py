#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and \
password) and uses the GitHub API to display your id.
"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get("https://api.github.com/repos/{}/{}/commits?per_page=10".
                     format(sys.argv[2], sys.argv[1]),
                     headers={'Accept': 'application/vnd.github.v3+json'})
    if r.status_code == 200:
        for i in r.json():
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
