#!/usr/bin/python3
"""
Module Docstring
"""


class Node:
    """
    Class Docstring
    """

    def __init__(self, data, next_node=None):
        """
        Initialize class Docstring
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Property method Docstring
        """
        return self.__data

    @data.setter
    def data(self, value: int):
        """
        Setter method Docstring
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Property method Docstring
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method Docstring
        """
        if not (value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Class Docstring
    """

    def __init__(self):
        """
        Initialize class Docstring
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Public instance method Docstring
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            c = self.__head
            p = None
            while c is not None and value > c.data:
                p = c
                c = c.next_node
            if c is None:
                p.next_node = Node(value)
            elif c is self.__head and p is None:
                self.__head = Node(value, c)
            else:
                new_node = Node(value, c)
                p.next_node = new_node

    def __str__(self):
        """
        Public instance method Docstring
        """
        h = self.__head
        lst = ""
        while h:
            lst += "{:d}".format(h.data)
            h = h.next_node
            if h:
                lst += "\n"
        return lst
