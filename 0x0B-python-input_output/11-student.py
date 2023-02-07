#!/usr/bin/python3
"""
Module Docstring
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        init function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to json function
        """
        if attrs is None:
            return {key: value for key, value in self.__dict__.items()}
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """
        reload_from_json
        """
        for key, value in json.items():
            setattr(self, key, value)
