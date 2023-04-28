#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL \
and displays the body of the response (decoded in utf-8).
"""

if __name__ == '__main__':
    from urllib import request, parse, error
    import sys

    r = request.Request(str(sys.argv[1]))
    try:
        with request.urlopen(r) as u:
            print(u.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
