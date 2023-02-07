#!/usr/bin/python3
"""
Module Docstring
"""
import json


def from_json_string(my_str):
    """
    from_json_string
    """
    return json.dumps(json.loads(my_str))
