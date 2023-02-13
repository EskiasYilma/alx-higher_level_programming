#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_Init(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 20, 30, 40, 50)

    def test_rectangle_is_instanceof_base(self):
        """Test that the Rectangle class is derived from the Base class"""
        self.assertIsInstance(self.r1, Base)

    def test_rectangle_width_pinstance(self):
        """Test that the width attribute is private"""
        with self.assertRaises(AttributeError):
            self.r1.__width

    def test_rectangle_width_getter(self):
        """Test width getter"""
        self.assertEqual(self.r1.width, 10)

    def test_rectangle_width_setter(self):
        """Test width setter"""
        self.r1.width = 30
        self.assertEqual(self.r1.width, 30)

        with self.assertRaises(ValueError):
            self.r1.width = -30

    def test_rectangle_height_pinstance(self):
        """Test that the height attribute is private"""
        with self.assertRaises(AttributeError):
            self.r1.__height

    def test_rectangle_height_getter(self):
        """Test height getter"""
        self.assertEqual(self.r1.height, 20)

    def test_rectangle_height_setter(self):
        """Test height setter"""
        self.r1.height = 30
        self.assertEqual(self.r1.height, 30)

        with self.assertRaises(ValueError):
            self.r1.height = -30

    def test_rectangle_x_pinstance(self):
        """Test private x attribute cannot be accessed directly"""
        with self.assertRaises(AttributeError):
            self.r1.__x

    def test_rectangle_x_getter(self):
        """Test x getter"""
        self.assertEqual(self.r1.x, 30)

    def test_rectangle_x_setter(self):
        """Test x setter"""
        self.r1.x = 30
        self.assertEqual(self.r1.x, 30)

        with self.assertRaises(ValueError):
            self.r1.x = -30

    def test_rectangle_y_pinstance(self):
        """Test private y attribute cannot be accessed directly"""
        with self.assertRaises(AttributeError):
            self.r1.__y

    def test_rectangle_y_getter(self):
        """Test y getter"""
        self.assertEqual(self.r1.y, 40)

    def test_rectangle_y_setter(self):
        """Test y setter"""
        self.r1.y = 30
        self.assertEqual(self.r1.y, 30)

        with self.assertRaises(ValueError):
            self.r1.y = -30

    def test_rectangle_init_no_args(self):
        """Test the error raised when no arguments are provided to the init method"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_rectangle_init_one_arg(self):
        """Test the error raised when only one argument is provided to the init method"""
        with self.assertRaises(TypeError):
            r = Rectangle(2)

    def test_rectangle_init_two_args_inst(self):
        """Test the init method with two arguments"""
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_init_three_args_inst(self):
        """Test the init method with three arguments"""
        r1 = Rectangle(2, 3, 1)
        r2 = Rectangle(2, 3, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_init_four_args_inst(self):
        """Test the init method with four arguments"""
        r1 = Rectangle(2, 3, 1, 2)
        r2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_init_five_args(self):
        """Test the init method with five arguments"""
        self.assertEqual(50, self.r1.id)

    def test_rectangle_init_more_than_five_args(self):
        """Test the error raised when more than five arguments are provided to the init method"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 1, 2, 3, 4)

    def test_area(self):
        """Test area"""
        self.assertEqual(self.r1.area(), 200)

    def test_display(self):
        """Test display"""
        self.assertIsNone(self.r1.display())

    def test_update(self):
        """Test update"""
        self.r1.update(100, 200, 300, 400, 500)
        self.assertEqual(self.r1.id, 100)
        self.assertEqual(self.r1.width, 200)
        self.assertEqual(self.r1.height, 300)
        self.assertEqual(self.r1.x, 400)
        self.assertEqual(self.r1.y, 500)
        self.r1.update(x=1000, height=2000, y=3000, width=4000, id=5000)
        self.assertEqual(self.r1.id, 5000)
        self.assertEqual(self.r1.width, 4000)
        self.assertEqual(self.r1.height, 2000)
        self.assertEqual(self.r1.x, 1000)
        self.assertEqual(self.r1.y, 3000)

    def test_to_dictionary(self):
        """Test to_dictionary"""
        expected = {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        self.assertEqual(self.r1.to_dictionary(), expected)


class TestRectangle_width(unittest.TestCase):
    """Test class for the width method of the Rectangle class"""

    def test_rectangle_with_float_width(self):
        """Test for float value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(7.2, 9)

    def test_rectangle_with_string_width(self):
        """Test for string value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("five", 1)

    def test_rectangle_with_list_width(self):
        """Test for list value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([5, 6], 1)

    def test_rectangle_with_dict_width(self):
        """Test for dictionary value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({5: 6}, 1)

    def test_rectangle_with_tuple_width(self):
        """Test for tuple value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((5, 6), 1)

    def test_rectangle_with_set_width(self):
        """Test for set value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({5, 6}, 1)

    def test_rectangle_with_frozenset_width(self):
        """Test for frozenset value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(frozenset([5, 6]), 1)

    def test_rectangle_with_bool_width(self):
        """Test for boolean value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_rectangle_with_None_width(self):
        """Test for None value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 1)

    def test_rectangle_with_int_width(self):
        """Test for integer value of width"""
        r = Rectangle(5, 1)
        self.assertIsInstance(r, Rectangle)

    def test_rectangle_with_neg_int_width(self):
        """Test for negative integer value of width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-5, 1)

    def test_rectangle_with_zero_width(self):
        """Test for zero value of width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)


class TestRectangle_height(unittest.TestCase):
    """Test class for the height method of the Rectangle class"""

    def test_rectangle_with_int_height(self):
        """Test height as integer"""
        r = Rectangle(1, 1)
        self.assertEqual(r.height, 1)

    def test_rectangle_with_float_height(self):
        """Test height as float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_rectangle_with_zero_height(self):
        """Test height as zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_rectangle_with_negative_height(self):
        """Test height as negative number"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_rectangle_with_str_height(self):
        """Test height as string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "1")

    def test_rectangle_with_list_height(self):
        """Test height as list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1])

    def test_rectangle_with_dict_height(self):
        """Test height as dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1: 1})

    def test_rectangle_with_tuple_height(self):
        """Test height as tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1,))

    def test_rectangle_with_set_height(self):
        """Test height as set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1})

    def test_rectangle_with_bool_height(self):
        """Test height as boolean"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)

    def test_rectangle_with_None_height(self):
        """Test height as None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_rectangle_with_inf_height(self):
        """Test height as infinity"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_rectangle_with_nan_height(self):
        """Test height as NaN"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))


class TestRectangle_x(unittest.TestCase):
    """Test cases for the x property of the Rectangle class."""

    def test_rectangle_with_int_x(self):
        """Test x as integer."""
        r = Rectangle(10, 10, x=10)
        self.assertEqual(r.x, 10)

    def test_rectangle_with_float_x(self):
        """Test x as float."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x=10.5)

    def test_rectangle_with_none_x(self):
        """Test x as None."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x=None)

    def test_rectangle_with_bool_x(self):
        """Test x as boolean."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x=True)

    def test_rectangle_with_list_x(self):
        """Test x as list."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x=[10])

    def test_rectangle_with_dict_x(self):
        """Test x as dictionary."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x={10: 20})

    def test_rectangle_with_str_x(self):
        """Test x as string."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x="10")

    def test_rectangle_with_tuple_x(self):
        """Test x as tuple."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x=(10, 20))

    def test_rectangle_with_set_x(self):
        """Test x as set."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, x={10})

    def test_rectangle_with_negative_x(self):
        """Test x as negative integer."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 10, x=-10)

    def test_rectangle_with_zero_x(self):
        """Test x as zero."""
        r = Rectangle(10, 10, x=0)
        self.assertEqual(r.x, 0)

    def test_rectangle_with_positive_x(self):
        """Test x as positive integer."""
        r = Rectangle(10, 10, x=10)
        self.assertEqual(r.x, 10)


class TestRectangle_x(unittest.TestCase):
    """Test for the y setter method of the Rectangle class"""

    def test_rectangle_with_int_y(self):
        """Test for a positive integer value"""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.y, 10)

    def test_rectangle_with_negative_y(self):
        """Test for a negative integer value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 10, 10, -10)

    def test_rectangle_with_zero_y(self):
        """Test for a zero value"""
        r = Rectangle(10, 10, 10, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_with_float_y(self):
        """Test for a float value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, 10.5)

    def test_rectangle_with_none_y(self):
        """Test for None value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, None)

    def test_rectangle_with_dict_y(self):
        """Test for a dictionary value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, {"y": 10})

    def test_rectangle_with_list_y(self):
        """Test for a list value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, [10])

    def test_rectangle_with_set_y(self):
        """Test for a set value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, {10})

    def test_rectangle_with_tuple_y(self):
        """Test for a tuple value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, (10,))

    def test_rectangle_with_bool_y(self):
        """Test for a boolean value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, True)

    def test_rectangle_with_str_y(self):
        """Test for a string value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, "10")

    def test_rectangle_with_bytes_y(self):
        """Test for a bytes value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, b"10")


if __name__ == "__main__":
    unittest.main()
