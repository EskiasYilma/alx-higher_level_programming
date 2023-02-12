#!/usr/bin/python3
"""
Unittest for Base Class
"""
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Init(unittest.TestCase):
    """Unittests for the init method of Base Class"""

    def setUp(self):
        """
        Setup testing environment
        """
        Base._Base__nb_objects = 0

    def test_init_default_id(self):
        """Test init with a complex number as an id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_init_multiple_default_id(self):
        """Test init with a multiple default instances as an id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_init_with_None_id(self):
        """Test init with a complex number as an id"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_init_with_integer_id(self):
        """Test init with a complex number as an id"""
        self.assertEqual(12, Base(12).id)

    def test_init_with_integer_and_default_id(self):
        """Test init with a complex number as an id"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_init_id_update(self):
        """Test init with an updated id"""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_init_with_string_id(self):
        """Test init with a string as an id"""
        self.assertEqual("hello", Base("hello").id)

    def test_init_with_float_id(self):
        """Test init with a float as an id"""
        self.assertEqual(5.5, Base(5.5).id)

    def test_init_with_boolean_id(self):
        """Test init with a bool as an id"""
        self.assertEqual(True, Base(True).id)

    def test_init_with_dictionary_id(self):
        """Test init with a dict as an id"""
        self.assertEqual({"x": 1, "y": 2}, Base({"x": 1, "y": 2}).id)

    def test_init_with_complex_id(self):
        """Test init with a complex number as an id"""
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_init_with_list_id(self):
        """Test init with a list as an id"""
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_init_with_tuple_id(self):
        """Test init with a tuple as an id"""
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_init_with_two_args(self):
        """Test init with two arguements"""
        with self.assertRaises(TypeError):
            Base(5, 5)

    def test_init_with_frozenset_id(self):
        """Test init with a frozenset as an id"""
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_init_with_range_id(self):
        """Test init with a complex number as an id"""
        self.assertEqual(range(4), Base(range(4)).id)

    def test_init_with_set_id(self):
        """Test init with a set as an id"""
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_init_with_bytes_id(self):
        """Test init with a byte as an id"""
        self.assertEqual(b'ALX', Base(b'ALX').id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for the to_json_string method of Base Class"""

    def setUp(self):
        """
        Setup testing environment
        """
        Base._Base__nb_objects = 0

    def test_to_json_string_with_empty_list(self):
        """
        Test if the function returns an empty string for an empty list.
        """
        self.assertEqual('[]', Base.to_json_string([]))

    def test_to_json_string_with_list_of_integers(self):
        """
        Test if the function returns a correct JSON string \
        representation of a list of integers.
        """
        self.assertEqual('[1, 2, 3]', Base.to_json_string([1, 2, 3]))

    def test_to_json_string_with_list_of_strings(self):
        """
        Test if the function returns a correct JSON string\
         representation of a list of strings.
        """
        self.assertEqual('["a", "b", "c"]',
                         Base.to_json_string(["a", "b", "c"]))

    def test_to_json_string_with_list_of_dictionaries(self):
        """
        Test if the function returns a correct JSON string\
         representation of a list of dictionaries.
        """
        self.assertEqual('[{"a": 1}, {"b": 2}]',
                         Base.to_json_string([{"a": 1}, {"b": 2}]))

    def test_to_json_string_with_list_of_lists(self):
        """
        Test if the function returns a correct JSON string\
         representation of a list of lists.
        """
        self.assertEqual('[[1, 2], [3, 4]]',
                         Base.to_json_string([[1, 2], [3, 4]]))

    def test_to_json_string_with_list_of_null(self):
        """
        Test if the function returns a correct JSON string\
         representation of a list of null values.
        """
        self.assertEqual('[null, null, null]',
                         Base.to_json_string([None, None, None]))

    def test_to_json_string_with_list_of_True(self):
        """
        Test if the function returns a correct JSON string\
         representation of a list of booleans.
        """
        self.assertEqual('[true, true, false]',
                         Base.to_json_string([True, True, False]))

    def test_to_json_string_with_list_of_float(self):
        """
        Test if the function returns a correct JSON string\
         representation of a list of floating-point numbers.
        """
        self.assertEqual('[1.1, 2.2, 3.3]',
                         Base.to_json_string([1.1, 2.2, 3.3]))

    def test_to_json_string_with_dict_with_multiple_keys(self):
        """Test to_json_string with a dictionary with multiple keys"""
        d = {"a": 1, "b": 2, "c": 3}
        expected = '{"a": 1, "b": 2, "c": 3}'
        self.assertEqual(expected, Base.to_json_string(d))

    def test_to_json_string_with_square(self):
        """Test to_json_string method with a square object"""
        s = Square(10, 20, 30)
        expected = '[{"x": 20, "y": 30, "id": 10, "width": 10, "height": 10}]'
        self.assertTrue(expected, Base.to_json_string([s.to_dictionary()]))

    def test_to_json_string_with_rectangle(self):
        """Test to_json_string method with a rectangle object"""
        r = Rectangle(10, 20, 30, 40)
        expected = '[{"x": 20, "y": 30, "id": 10, "width": 40, "height": 20}]'
        self.assertTrue(expected, Base.to_json_string([r.to_dictionary()]))

    def test_to_json_string_with_multiple_shapes(self):
        """Test to_json_string method with multiple shapes"""
        s = Square(10, 20, 30)
        r = Rectangle(11, 21, 31, 41)
        expected = '[{"x": 20, "y": 30, "id": 10, "width": 10, \
        "height": 10},' + '{"x": 21, "y": 31, "id": 11, \
        "width": 41, "height": 21}]'
        self.assertTrue(expected, Base.to_json_string([s.to_dictionary(),
                                                       r.to_dictionary()]))

    def test_to_json_string_with_multiple_square_instances(self):
        """Test the to_json_string method with multiple Square instances"""
        s1 = Square(10, 10, 10)
        s2 = Square(11, 11, 11)
        s3 = Square(12, 12, 12)
        list_of_squares = [
            s1.to_dictionary(), s2.to_dictionary(), s3.to_dictionary()]
        expected = '[{"x": 10, "y": 10, "id": 10, "size": 10}, ' \
                   '{"x": 11, "y": 11, "id": 11, "size": 11}, ' \
                   '{"x": 12, "y": 12, "id": 12, "size": 12}]'
        self.assertTrue(expected, Base.to_json_string(list_of_squares))

    def test_to_json_string_with_multiple_rectangle_instances(self):
        """Test the to_json_string method with multiple Rectangle instances"""
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(11, 11, 11, 11)
        r3 = Rectangle(12, 12, 12, 12)
        list_of_rectangles = [
            r1.to_dictionary(), r2.to_dictionary(), r3.to_dictionary()]
        expected = '[{"x": 10, "y": 10, "id": 10, "width": 10, "height": 10}, \
        ''{"x": 11, "y": 11, "id": 11, "width": 11, "height": 11}, ' \
                   '{"x": 12, "y": 12, "id": 12, "width": 12, "height": 12}]'
        self.assertTrue(expected, Base.to_json_string(list_of_rectangles))

    def test_to_json_string_with_no_args(self):
        """Test that the to_json_string method raises a TypeError\
         if it is passed no arguements"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_with_multiple_int_args(self):
        """Test that the to_json_string method raises a TypeError\
         if it is passed multiple int args"""
        with self.assertRaises(TypeError):
            Base.to_json_string(123, "ALX")

    def test_to_json_string_with_list_of_complex(self):
        """
        Test if the function returns a correct JSON string \
        representation of a list of complex numbers.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string([1 + 2j, 3 + 4j, 5 + 6j])


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for the save_to_file method of Base Class"""

    def setUp(self):
        """
        Setup testing environment
        """
        Base._Base__nb_objects = 0

    def test_save_to_file_with_multiple_rectangle_instances(self):
        """ Tests if the function can save and read the file \
        with multiple rectangle instances"""
        r1 = Rectangle(5, 7, 2, 8, 2)
        r2 = Rectangle(9, 2, 1, 6, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 104)

    def test_save_to_file_with_empty_list(self):
        """ Tests if the function can save and read an empty file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_multiple_square_instances(self):
        """ Tests if the function can save and read the \
        file with multiple square instances"""
        s1 = Square(15, 7, 2, 8)
        s2 = Square(19, 2, 1, 6)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 78)

    def test_save_to_file_with_empty_list_of_squares(self):
        """ Tests if the function can save and read an empty file of squares"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_one_rectangle_instance(self):
        """Tests if the function can save and read a file\
         with a single rectangle instance"""
        rect = Rectangle(11, 8, 29, 91, 96)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 56)

    def test_save_to_file_with_none_arg(self):
        """Tests if the function can handle None as an argument"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_with_incorrect_arg_type(self):
        """Tests if the function raises a TypeError when\
         an incorrect argument type is passed"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file("Hello", [])

    def test_save_to_file_with_incorrect_number_of_args(self):
        """Tests if the function raises a TypeError when\
         the incorrect number of arguments are passed"""
        with self.assertRaises(TypeError):
            Square.save_to_file(1, 2)

    def clean_slate(self):
        """Delete all JSON files that were created before running the tests."""
        for i in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(i)
            except IOError:
                pass


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for the from_json_string method of Base Class"""

    def test_from_json_string(self):
        """Test the from_json_string method of the Base class"""
        json_txt = [{"id": 1, "width": 20, "height": 30, "x": 40, "y": 50}, {
            "id": 2, "width": 10, "height": 10, "x": 0, "y": 0}]
        json_string = Rectangle.to_json_string(json_txt)
        objects = Rectangle.from_json_string(json_string)
        self.assertEqual(len(objects), 2)
        self.assertIsInstance(objects, list)
        self.assertIsInstance(objects[0], dict)
        self.assertIsInstance(objects[1], dict)
        self.assertEqual(objects[0]["id"], 1)
        self.assertEqual(objects[0]["width"], 20)
        self.assertEqual(objects[0]["height"], 30)
        self.assertEqual(objects[0]["x"], 40)
        self.assertEqual(objects[0]["y"], 50)
        self.assertEqual(objects[1]["id"], 2)
        self.assertEqual(objects[1]["width"], 10)
        self.assertEqual(objects[1]["height"], 10)
        self.assertEqual(objects[1]["x"], 0)
        self.assertEqual(objects[1]["y"], 0)

    def test_from_json_string_empty(self):
        """Test the from_json_string method of the Base class\
         with an empty string"""
        json_string = ''
        objects = Base.from_json_string(json_string)
        self.assertEqual(objects, [])

    def test_from_json_string_with_one_rectangle_object(self):
        """ Test for JSON string with one object"""
        json_txt = [{"id": 1, "width": 20, "height": 30, "x": 40, "y": 50}]
        json_string = Rectangle.to_json_string(json_txt)
        objects = Rectangle.from_json_string(json_string)
        self.assertEqual(len(objects), 1)
        self.assertIsInstance(objects, list)
        self.assertIsInstance(objects[0], dict)
        self.assertEqual(objects[0]["id"], 1)
        self.assertEqual(objects[0]["width"], 20)
        self.assertEqual(objects[0]["height"], 30)
        self.assertEqual(objects[0]["x"], 40)
        self.assertEqual(objects[0]["y"], 50)

    def test_from_json_string_with_multiple_rectangle_objects(self):
        """ Test for JSON string with multiple objects"""
        json_txt = [{"id": 1, "width": 20, "height": 30, "x": 40, "y": 50}, {
            "id": 2, "width": 10, "height": 10, "x": 0, "y": 0}]
        json_string = Rectangle.to_json_string(json_txt)
        objects = Rectangle.from_json_string(json_string)
        self.assertEqual(len(objects), 2)
        self.assertIsInstance(objects, list)
        self.assertIsInstance(objects[0], dict)
        self.assertIsInstance(objects[1], dict)
        self.assertEqual(objects[0]["id"], 1)
        self.assertEqual(objects[0]["width"], 20)
        self.assertEqual(objects[0]["height"], 30)
        self.assertEqual(objects[0]["x"], 40)
        self.assertEqual(objects[0]["y"], 50)
        self.assertEqual(objects[1]["id"], 2)
        self.assertEqual(objects[1]["width"], 10)
        self.assertEqual(objects[1]["height"], 10)
        self.assertEqual(objects[1]["x"], 0)
        self.assertEqual(objects[1]["y"], 0)


class TestBase_create(unittest.TestCase):
    """Unittests for the create method of Base Class"""

    def test_create_with_square(self):
        """Test the create method of the Base class with square"""
        s1 = Square(19, 2, 1, 6)
        self.assertIsInstance(s1, Square)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual("[Square] (6) 2/1 - 19", str(s1))

    def test_create_with_rectangle(self):
        """Test the create method of the Base class with rectangle"""
        r1 = Rectangle(19, 18, 2, 1, 6)
        self.assertIsInstance(r1, Rectangle)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (6) 2/1 - 19/18", str(r1))

    def test_create_with_rectangle_comparision_is(self):
        """Test the create method of the Base class with rectangle"""
        r1 = Rectangle(19, 18, 2, 1, 6)
        self.assertIsInstance(r1, Rectangle)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_with_square_comparision_is(self):
        """Test the create method of the Base class with square"""
        s1 = Square(19, 2, 1, 6)
        self.assertIsInstance(s1, Square)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_create_with_string_id(self):
        """Test the create method of the Base class with string id"""
        with self.assertRaises(TypeError):
            r1 = Square.create("1")

    def test_create_with_float_id(self):
        """Test the create method of the Base class with float id"""
        with self.assertRaises(TypeError):
            r1 = Base.create(1.5)

    def test_create_with_bool_id(self):
        """Test the create method of the Base class with bool id"""
        with self.assertRaises(TypeError):
            r1 = Base.create(True)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for the save_to_file_csv method of Base Class"""

    def setUp(self):
        """
        Setup testing environment
        """
        Base._Base__nb_objects = 0

    def test_load_from_file_valid_file(self):
        """
        test_load_from_file_valid_file
        """
        r1 = Rectangle(10, 33, 53, 6)
        r2 = Rectangle(122, 767)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(len(Rectangle.load_from_file()), 2)

    def test_load_from_file_file_types_rectangle(self):
        """
        test_load_from_file_file_types_rectangle
        """
        r1 = Rectangle(10, 33, 53, 6)
        r2 = Rectangle(122, 767)
        Rectangle.save_to_file([r1, r2])
        load = Rectangle.load_from_file()
        self.assertTrue((type(i) == Rectangle for i in str(load)))

    def test_load_from_file_file_types_square(self):
        """
        test_load_from_file_file_types_square
        """
        r1 = Square(10, 33, 53, 6)
        r2 = Square(122, 767)
        Square.save_to_file([r1, r2])
        load = Square.load_from_file()
        self.assertTrue((type(i) == Square for i in str(load)))

    def test_load_from_file_empty_file(self):
        """
        test_load_from_file_empty_file
        """
        open("Rectangle.json", "w").close()
        self.assertEqual(len(Rectangle.load_from_file()), 0)

    def test_load_from_file_invalid_data(self):
        """
        test_load_from_file_invalid_data
        """
        with open("Rectangle.json", "w") as file:
            file.write("{'width': 10}")
        with self.assertRaises(json.decoder.JSONDecodeError):
            Rectangle.load_from_file()

    def test_load_from_file_invalid_json(self):
        """
        test_load_from_file_invalid_json
        """
        with open("Rectangle.json", "w") as file:
            file.write("width: 10")
        with self.assertRaises(ValueError):
            Rectangle.load_from_file()

    def clean_slate(self):
        """Delete all JSON files that were created before running the tests."""
        for i in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(i)
            except IOError:
                pass


class TestBase_save_to_file_csv(unittest.TestCase):

    """Unittests for the save_to_file_csv method of Base Class"""

    def setUp(self):
        """
        Setup testing environment
        """
        Base._Base__nb_objects = 0

    def test_save_to_file_csv_with_multiple_rectangle_instances(self):
        """ Tests if the function can save and read the file\
         with multiple rectangle instances"""
        r1 = Rectangle(51, 73, 29, 82, 24)
        r2 = Rectangle(60, 40, 20, 50, 45)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertEqual(file_contents[0], '24,51,73,29,82')
            self.assertEqual(file_contents[1], '45,60,40,20,50')

    def test_save_to_file_csv_with_single_rectangle_instance(self):
        """
        Test if the function can save and read the file\
         with a single rectangle instance
        """
        r = Rectangle(51, 73, 29, 82, 24)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertEqual(file_contents[0], '24,51,73,29,82')

    def test_save_to_file_csv_with_multiple_square_instances(self):
        """
        Test if the function can save and read the file\
         with multiple square instances
        """
        s1 = Square(40, 20, 50, 45)
        s2 = Square(30, 30, 10, 10)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertEqual(file_contents[0], '45,40,20,50')
            self.assertEqual(file_contents[1], '10,30,30,10')

    def test_save_to_file_csv_with_single_square_instance(self):
        """
        Test if the function can save and read the file\
         with a single square instance
        """
        s = Square(40, 20, 50, 45)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertEqual(file_contents[0], '45,40,20,50')

    def test_save_to_file_csv_with_class_name_instance(self):
        """
        Test if the function can save and read the file\
         with a base instance of a single square
        """
        s = Square(40, 20, 50, 45)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertTrue('45,40,20,50', file_contents[0])

    def test_save_to_file_csv_with_empty_list(self):
        """
        Test if the function can save and read the file with an empty list
        """
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertEqual(file_contents, [''])

    def test_save_to_file_csv_with_more_than_one_arguement(self):
        """
        Test if the function can save the file with a more than one arguement
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(3, 5)

    def test_save_to_file_csv_with_None_arguments(self):
        """
        Test if the function can save the file with None arguement
        """
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            file_contents = f.read().split('\n')
            self.assertEqual(file_contents, [''])

    def test_save_to_file_csv_with_no_arguments(self):
        """
        Test if the function can save the file with no arguements
        """
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

    def clean_slate(self):
        """Delete all CSV files that were created while running the tests."""
        for i in ["Rectangle.csv", "Square.csv", "Base.csv"]:
            try:
                os.remove(i)
            except IOError:
                pass


class TestBase_load_from_file_csv(unittest.TestCase):

    """Unittests for the save_to_file_csv method of Base Class"""

    def setUp(self):
        """
        Setup testing environment
        """
        Base._Base__nb_objects = 0

    def test_load_from_file_csv_with_Multiple_rectangle_instances(self):
        """ Tests if the function can save and read the file\
         with multiple rectangle instances"""
        r1 = Rectangle(51, 73, 29, 82, 24)
        r2 = Rectangle(60, 40, 20, 50, 45)
        r_list = [r1, r2]
        Rectangle.save_to_file_csv(r_list)
        csv_file = Rectangle.load_from_file_csv()
        for i, j in enumerate(r_list):
            self.assertEqual(str(j), str(csv_file[i]))

    def test_load_from_file_csv_with_single_rectangle_instance(self):
        """ Tests if the function can save and read the file\
         with single rectangle instance"""
        r1 = Rectangle(51, 73, 29, 82, 24)
        r_list = [r1]
        Rectangle.save_to_file_csv(r_list)
        csv_file = Rectangle.load_from_file_csv()
        for i, j in enumerate(r_list):
            self.assertEqual(str(j), str(csv_file[i]))

    def test_load_from_file_csv_with_single_square_instance(self):
        """ Tests if the function can save and read the file\
         with single square instance"""
        s = Square(40, 20, 50, 45)
        Square.save_to_file_csv([s])
        csv_file = Square.load_from_file_csv()
        self.assertEqual(str(s), str(csv_file[0]))

    def test_load_from_file_csv_with_multiple_square_instances(self):
        """ Tests if the function can save and read the file\
         with multiple square instances"""
        s = Square(40, 20, 50, 45)
        s2 = Square(41, 22, 55, 44)
        s_list = [s, s2]
        Square.save_to_file_csv(s_list)
        csv_file = Square.load_from_file_csv()
        for i, j in enumerate(s_list):
            self.assertEqual(str(j), str(csv_file[i]))

    def test_load_from_file_csv_for_types(self):
        """
        Test if the function can identify correct types
        """
        s = Square(40, 20, 50, 45)
        s2 = Square(41, 22, 55, 44)
        s_list = [s, s2]
        Square.save_to_file_csv(s_list)
        csv_file = Square.load_from_file_csv()
        for i, j in enumerate(s_list):
            self.assertIsInstance(csv_file[i], Square)

    def test_load_from_file_csv_with_more_than_one_arguement(self):
        """ Tests if the function can take more than one arguement"""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv(3, 5)

    def test_load_from_file_csv_with_no_file(self):
        """ Tests if the function can read no file"""
        self.clean_slate()
        csv_file = Square.load_from_file_csv()
        self.assertEqual([], csv_file)

    def clean_slate(self):
        """Delete all CSV files that were created while running the tests."""
        for i in ["Rectangle.csv", "Square.csv", "Base.csv"]:
            try:
                os.unlink(i)
            except IOError:
                continue


if __name__ == "__main__":
    unittest.main()
