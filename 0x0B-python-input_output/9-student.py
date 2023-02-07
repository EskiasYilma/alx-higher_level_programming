#!/usr/bin/python3
"""
Module Docstring
"""


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

    def to_json(self):
        """
        to json function
        """
        return {key: value for key, value in self.__dict__.items()}
