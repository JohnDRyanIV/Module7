import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            topic1.make_list()  # call the function!

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-3')  # patch function for input
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):  # Below 1
            topic1.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='58')  # patch function for input
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):  # Above 50
            topic1.make_list()
