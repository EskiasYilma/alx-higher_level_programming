#!/usr/bin/python3
"""
Module Docstring
"""


def add_attribute(object, name, attr):
    """
    add_attribute Function
    """
    if getattr(object, "__doc__", None) is None:
        setattr(object, name, attr)
    else:
        raise TypeError("can't add new attribute")


class MyClass():
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
