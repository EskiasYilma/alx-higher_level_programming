#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST \
request to the passed URL with the email as a parameter, \
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    from urllib import request, parse
    import sys

    email = parse.urlencode([('email':str(sys.argv[2]))])
    with request.Request(str(sys.argv[1]), data=email) as u:
        resp = request.urlopen(u)
        print(resp.read().decode('utf-8'))
