#!/usr/bin/python3
"""
Module Docstring
"""
import sys
import signal

if __name__ == '__main__':

    def signal_handler(signal, frame):
        """
        signal_handler
        """
        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            print("{}: {}".format(key, value))
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    status_codes = {}
    file_size = 0
    counter = 0

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        counter += 1
        try:
            items = line.split(" ")
            status = int(items[-2])
            size = int(items[-1])
            if status not in status_codes:
                status_codes[status] = 0
            status_codes[status] += 1
            file_size += size
        except:
            continue
        if counter == 10:
            print("File size: {}".format(file_size))
            for key, value in sorted(status_codes.items()):
                print("{}: {}".format(key, value))
            counter = 0
