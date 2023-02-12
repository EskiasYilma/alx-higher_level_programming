#!/usr/bin/python3

"""
Square Module Docstring
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class Docstring
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init Function Docstring
        Class Constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size Function Docstring
        Return: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size Function Docstring
        sets size
        """
        self.width = value
        self.height = value

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
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        if self.size is None:
            self.__init__(0)

    def to_dictionary(self):
        """
        to_dictionary Function Docstring
        Return: the dictionary representation of a Square:
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        __str__ Function Docstring
        Return: [Square] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
