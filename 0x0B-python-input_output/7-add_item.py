#!/usr/bin/python3
"""
Module Docstring
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_to_list(args):
    if os.path.isfile("add_item.json"):
        if os.path.getsize('add_item.json') == 0:
            save_to_json_file([], "add_item.json")
        else:
            data = load_from_json_file("add_item.json")
            if args:
                for i in args[1:]:
                    data.append(i)
                save_to_json_file(data, "add_item.json")
    else:
        save_to_json_file([], "add_item.json")


if __name__ == "__main__":
    add_to_list(sys.argv)
