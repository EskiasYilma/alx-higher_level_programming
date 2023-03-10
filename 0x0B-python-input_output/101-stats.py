#!/usr/bin/python3
"""
Module Docstring
"""

import sys


def tokenize(line):
    """
    tokenize docstring
    """
    elements = line.split()
    status_code = int(elements[-2])
    file_size = int(elements[-1])
    return status_code, file_size


def update_data(metrics, status_code, file_size):
    """
    update_data docstring
    """
    metrics['ttl_size'] += file_size
    if status_code in metrics['stat_codes']:
        metrics['stat_codes'][status_code] += 1
    else:
        metrics['stat_codes'][status_code] = 1


def print_metrics(metrics):
    """
    print_metrics docstring
    """
    print("File size: {}".format(metrics['ttl_size']))
    for status_code in sorted(metrics['stat_codes'].keys()):
        if str(status_code) in ['200', '301', '400', '401',
                                '403', '404', '405', '500']:
            print("{}: {}".format(status_code,
                                  metrics['stat_codes'][status_code]))


def main():
    """
    main docstring
    """
    metrics = {'ttl_size': 0, 'stat_codes': {}}
    lines_read = 0
    try:
        for line in sys.stdin:
            status_code, file_size = tokenize(line)
            update_data(metrics, status_code, file_size)
            lines_read += 1
            if lines_read % 10 == 0:
                print_metrics(metrics)
    except KeyboardInterrupt:
        print_metrics(metrics)
        raise


if __name__ == '__main__':
    main()
