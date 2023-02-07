#!/usr/bin/python3
"""
Module Docstring
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file
    """
    with open(filename, 'r') as f:
        return json.load(f)
