#!/usr/bin/python3
"""
Module Docstring
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_to_list(args):
    """
    add_to_list
    """
    try:
        data = load_from_json_file("add_item.json")
    except Exception:
        data = []
        pass

    for i in args[1:]:
        data.append(i)
    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    add_to_list(sys.argv)
