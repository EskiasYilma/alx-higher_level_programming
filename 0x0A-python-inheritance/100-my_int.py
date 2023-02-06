#!/usr/bin/python3
"""
Module Docstring
"""


class MyInt(int):
    """
    MyInt the Rebel
    """

    def __ne__(self, comp):
        return (self - comp == 0)

    def __eq__(self, comp):
        return (self - comp != 0)
