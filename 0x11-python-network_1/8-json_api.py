#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to\
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        data = {"q": str(sys.argv[1])}
    except Exception:
        data = {"q": ""}

    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        if len(r.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except Exception:
        print("Not a valid JSON")
