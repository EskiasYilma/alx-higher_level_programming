#!/usr/bin/python3

"""
Rectangle Module Docstring
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class Docstring
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init Function Docstring
        Class Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width Function Docstring
        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width Function Docstring
        sets width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height Function Docstring
        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height Function Docstring
        sets height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x Function Docstring
        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x Function Docstring
        sets x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y Function Docstring
        Return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y Function Docstring
        sets y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area Function Docstring
        Return: the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        display Function Docstring
        Return: prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        __str__ Function Docstring
        Return: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        update Function Docstring
        assigns an argument to each attribute:

            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    if arg is None:
                        self.__init__(self, self.width,
                                      self.height, self.x, self.y)
                    else:
                        self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self, self.width,
                                      self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if self.width is None or self.height is None:
            self.__init__(0, 0)

    def to_dictionary(self):
        """
        to_dictionary Function Docstring
        Return: the dictionary representation of a Rectangle:
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
