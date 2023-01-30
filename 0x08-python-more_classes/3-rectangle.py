#!/usr/bin/python3
"""
Module DOcstring
"""


class Rectangle:
    """
    Class Docstring
    """

    def __init__(self, width=0, height=0):
        """
        Init Docstring
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property Method docstring
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter Method Docstring
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property Method docstring
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter Method Docstring
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method Docstring
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method Docstring
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Public instance method Docstring
        """
        rec = ""
        if self.__width < 0 or self.__height < 0:
            return rec
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec += "#"
                if i is not (self.__height - 1):
                    rec += "\n"
                else:
                    pass
            return rec
