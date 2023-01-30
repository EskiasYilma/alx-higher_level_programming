#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger Class Docstring
    """

    def test_empty(self):
        """
        test_empty Function Docstring
        Tests for empty list
        """
        self.assertIsNone(max_integer([]))

    def test_integers(self):
        """
        test_integers Function Docstring
        Tests for max integer for positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negatives(self):
        """
        test_negatives Function Docstring
        Tests for max integer for negetive numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)


if __name__ == '__main__':
    unittest.main()
