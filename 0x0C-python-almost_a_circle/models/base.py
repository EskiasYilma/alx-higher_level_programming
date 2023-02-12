#!/usr/bin/python3

"""
Base Module Docstring
"""

import json
import csv
import turtle


class Base:
    """
    Base Class Docstring
    _nb_objects : number of base instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init Function Docstring
        Class Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string Function Docstring
        Return: the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file Function Docstring
        Return: writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        dict_objs = [obj.to_dictionary() for obj in list_objs]
        json_string = Base.to_json_string(dict_objs)
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string Function Docstring
        Return: the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create Function Docstring
        Return: an instance with all attributes already set:
        """
        if dictionary != {} and dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file Function Docstring
        Return: returns a list of instances
        """
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                json_string = f.read()
            dict_objs = Base.from_json_string(json_string)
            return [cls.create(**obj) for obj in dict_objs]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv Function Docstring
        Return: serializes in CSV
        """
        if list_objs is None or list_objs == []:
            list_objs = []
        with open("{}.csv".format(cls.__name__), 'w', newline='') as f:
            writer = csv.writer(f)

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv Function Docstring
        Return: deserializes in CSV
        """
        try:
            with open("{}.csv".format(cls.__name__), 'r') as f:
                # rows = []
                if cls.__name__ == "Rectangle":
                    rows = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    rows = ["id", "size", "x", "y"]

                objs = [dict([key, int(value)] for key, value in read_dict.
                             items())for read_dict in csv.DictReader
                        (f, fieldnames=rows)]
                return [cls.create(**obj) for obj in objs]

        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw Function Docstring
        Return: opens a window and draws all the Rectangles and Squares
        """
        t = turtle.Turtle()
        t.speed("fastest")
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.fd(rect.width)
            t.right(90)
            t.fd(rect.height)
            t.right(90)
            t.fd(rect.width)
            t.right(90)
            t.fd(rect.height)
        for sq in list_squares:
            t.penup()
            t.goto(sq.x, sq.y)
            t.pendown()
            for i in range(4):
                t.fd(sq.size)
                t.right(90)
        turtle.done()
