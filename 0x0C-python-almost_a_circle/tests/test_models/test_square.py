#!/usr/bin/python3
"""
Unittest for Square Class
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare_Init(unittest.TestCase):
    """Unittests for the init method of the Square class"""

    def setUp(self):
        """
        setup testing environment
        """
        self.s1 = Square(10, 20, 30, 40)

    def test_square_is_instanceof_rectangle(self):
        """Test that the Square class is derived from the Base class"""
        self.assertIsInstance(self.s1, Rectangle)
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s1, Base)

    def test_square_is_instanceof_base(self):
        """Test that the Square class is derived from the Base class"""
        self.assertIsInstance(self.s1, Base)

    def test_square_size_pinstance(self):
        """Test that the size attribute is private"""
        with self.assertRaises(AttributeError):
            self.s1.__size

    def test_square_size_getter(self):
        """Test size getter"""
        self.assertEqual(self.s1.size, 10)

    def test_square_size_setter(self):
        """Test size setter"""
        self.s1.size = 30
        self.assertEqual(self.s1.size, 30)

        with self.assertRaises(ValueError):
            self.s1.size = -30

    def test_square_x_pinstance(self):
        """Test private x attribute cannot be accessed directly"""
        with self.assertRaises(AttributeError):
            self.s1.__x

    def test_square_x_getter(self):
        """Test x getter"""
        self.assertEqual(self.s1.x, 20)

    def test_square_x_setter(self):
        """Test x setter"""
        self.s1.x = 30
        self.assertEqual(self.s1.x, 30)

        with self.assertRaises(ValueError):
            self.s1.x = -30

    def test_square_y_pinstance(self):
        """Test private y attribute cannot be accessed directly"""
        with self.assertRaises(AttributeError):
            self.s1.__y

    def test_square_y_getter(self):
        """Test y getter"""
        self.assertEqual(self.s1.y, 30)

    def test_square_y_setter(self):
        """Test y setter"""
        self.s1.y = 30
        self.assertEqual(self.s1.y, 30)

        with self.assertRaises(ValueError):
            self.s1.y = -30

    def test_square_init_no_args(self):
        """Test the error raised when no arguments are \
        provided to the init method"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_square_init_one_arg(self):
        """Test the when only one argument is \
        provided to the init method"""
        s1 = Square(10)
        s2 = Square(20)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_init_no_args(self):
        """Test the error raised when no arguments are provided\
         to the init method"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_square_init_one_arg(self):
        """Test the error raised when only one argument is provided \
        to the init method"""
        s1 = Square(10)
        s2 = Square(20)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_init_two_args_inst(self):
        """Test the init method with two arguments"""
        s1 = Square(2, 3)
        s2 = Square(2, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_init_three_args_inst(self):
        """Test the init method with three arguments"""
        s1 = Square(2, 3, 1)
        s2 = Square(2, 3, 4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_init_four_args(self):
        """Test the init method with four arguments"""
        self.assertEqual(40, self.s1.id)

    def test_square_init_more_than_four_args(self):
        """Test the error raised when more than four arguments are provided\
         to the init method"""
        with self.assertRaises(TypeError):
            Square(2, 3, 1, 2, 3)

    def test_square_str(self):
        """Test the string representation of Square"""
        s1 = Square(2)
        s2 = Square(20, 20, 10)
        s3 = Square(3, 2, 18)

        self.assertEqual(s1.__str__(), '[Square] ({}) 0/0 - 2'.format(s1.id))
        self.assertEqual(
            s2.__str__(), '[Square] ({}) 20/10 - 20'.format(s2.id))
        self.assertEqual(s3.__str__(), '[Square] ({}) 2/18 - 3'.format(s3.id))

    def test_square_area(self):
        """Test the area method of Square"""
        s1 = Square(2)
        s2 = Square(20, 20, 10)
        s3 = Square(3, 2, 18)

        self.assertEqual(s1.area(), 4)
        self.assertEqual(s2.area(), 400)
        self.assertEqual(s3.area(), 9)

    def test_square_update(self):
        """Test the update method of Square"""
        s1 = Square(2)
        s2 = Square(20, 20, 10)
        s3 = Square(3, 2, 18)

        s1.update(20, 20, 10)
        s2.update(2)
        s3.update(18, 18, 18, id=18)

        self.assertEqual(s1.__str__(), '[Square] ({}) 10/0 - 20'.format(s1.id))
        self.assertEqual(str(s2), '[Square] ({}) 20/10 - 20'.format(s2.id))
        self.assertEqual(str(s3), '[Square] ({}) 18/18 - 18'.format(s3.id))

    def test_square_update_kwargs(self):
        """Test the update method with kwargs of Square"""
        s1 = Square(2)
        s2 = Square(20, 20, 10)
        s3 = Square(3, 20, 18)

        s1.update(size=18, x=20, y=3)
        self.assertEqual(s1.size, 18)
        self.assertEqual(s1.x, 20)
        self.assertEqual(s1.y, 3)

        s2.update(size=18, x=20, y=3)
        self.assertEqual(s2.size, 18)
        self.assertEqual(s2.x, 20)
        self.assertEqual(s2.y, 3)

        s3.update(size=18, x=20, y=3)
        self.assertEqual(s3.size, 18)
        self.assertEqual(s3.x, 20)
        self.assertEqual(s3.y, 3)

    def test_display(self):
        """Test display"""
        self.assertIsNone(self.s1.display())

    def test_to_dictionary(self):
        """Test to_dictionary"""
        expected = {'id': 40, 'size': 10, 'x': 20, 'y': 30}
        self.assertEqual(self.s1.to_dictionary(), expected)


class TestSquare_size(unittest.TestCase):
    """Unittests for the size method of the Square class"""

    def test_square_with_float_size(self):
        """Test for float value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(7.2)

    def test_square_with_string_size(self):
        """Test for string value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("five")

    def test_square_with_list_size(self):
        """Test for list value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([5, 6])

    def test_square_with_dict_size(self):
        """Test for dictionary value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square({5: 6})

    def test_square_with_tuple_size(self):
        """Test for tuple value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square((5, 6))

    def test_square_with_set_size(self):
        """Test for set value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square({5, 6})

    def test_square_with_frozenset_size(self):
        """Test for frozenset value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(frozenset([5, 6]))

    def test_square_with_bool_size(self):
        """Test for boolean value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_square_with_None_size(self):
        """Test for None value of size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(None)

    def test_square_with_int_size(self):
        """Test for integer value of size"""
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_square_with_neg_int_size(self):
        """Test for negative integer value of size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-5)

    def test_square_with_zero_size(self):
        """Test for zero value of size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)


class TestSquare_x(unittest.TestCase):
    """Test cases for the x property of the Square class."""

    def test_square_with_int_x(self):
        """Test x as integer."""
        s = Square(10, x=10)
        self.assertEqual(s.x, 10)

    def test_square_with_float_x(self):
        """Test x as float."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x=10.5)

    def test_square_with_none_x(self):
        """Test x as None."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x=None)

    def test_square_with_bool_x(self):
        """Test x as boolean."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x=True)

    def test_square_with_list_x(self):
        """Test x as list."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x=[10])

    def test_square_with_dict_x(self):
        """Test x as dictionary."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x={10: 20})

    def test_square_with_str_x(self):
        """Test x as string."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x="10")

    def test_square_with_tuple_x(self):
        """Test x as tuple."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x=(10, 20))

    def test_square_with_set_x(self):
        """Test x as set."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x={10})

    def test_square_with_negative_x(self):
        """Test x as negative integer."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, x=-10)

    def test_square_with_zero_x(self):
        """Test x as zero."""
        s = Square(10, x=0)
        self.assertEqual(s.x, 0)

    def test_square_with_positive_x(self):
        """Test x as positive integer."""
        s = Square(10, x=10)
        self.assertEqual(s.x, 10)


class TestSquare_y(unittest.TestCase):
    """Test for the y setter method of the Square class"""

    def test_square_with_int_y(self):
        """Test for a positive integer value"""
        s = Square(10, 10, 10)
        self.assertEqual(s.y, 10)

    def test_square_with_negative_y(self):
        """Test for a negative integer value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 10, -10)

    def test_square_with_zero_y(self):
        """Test for a zero value"""
        s = Square(10, 10, 0)
        self.assertEqual(s.y, 0)

    def test_square_with_float_y(self):
        """Test for a float value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, 10.5)

    def test_square_with_none_y(self):
        """Test for None value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, None)

    def test_square_with_dict_y(self):
        """Test for a dictionary value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, {"y": 10})

    def test_square_with_list_y(self):
        """Test for a list value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, [10])

    def test_square_with_set_y(self):
        """Test for a set value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, {10})

    def test_square_with_tuple_y(self):
        """Test for a tuple value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, (10,))

    def test_square_with_bool_y(self):
        """Test for a boolean value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, True)

    def test_square_with_str_y(self):
        """Test for a string value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, "10")

    def test_square_with_bytes_y(self):
        """Test for a bytes value"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, b"10")
