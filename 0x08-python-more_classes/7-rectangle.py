#!/usr/bin/python3
"""
Module DOcstring
"""


class Rectangle:
    """
    Class Docstring
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init Docstring
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return rec
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    try:
                        rec += str(self.print_symbol)
                    except Exception:
                        rec += type(self).print_symbol
                if i is not (self.__height - 1):
                    rec += "\n"
        return rec

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
