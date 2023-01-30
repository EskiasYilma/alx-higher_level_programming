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
        test_empty

        Tests for max_integer using an empty list
        """
        self.assertIsNone(max_integer([]), None)

    def test_positives(self):
        """
        test_positives

        Tests for max_integer using a list with positive integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negatives(self):
        """
        test_negatives

        Tests for max_integer using a list with negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_positive_and_negative(self):
        """
        test_positive_and_negative

        Tests for max_integer using a list with both positive and negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, 4, 5]), 5)
        self.assertEqual(max_integer([-5, 4, 3, 2, 1]), 4)

    def test_length_one(self):
        """
        test_length_one

        Tests for max_integer using a list with only one integer (positive or negative)
        """
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)


if __name__ == '__main__':
    unittest.main()
