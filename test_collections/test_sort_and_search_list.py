import unittest
from fun_with_collections import sort_and_search_list as lister


class MyTestCase(unittest.TestCase):
    def test_item_found(self):
        self.assertEqual(lister.search_list([1, 2, 37, 48], 37), 2)

    def test_item_not_found(self):
        self.assertEqual(lister.search_list([1, 2, 37, 48], 543), -1)




if __name__ == '__main__':
    unittest.main()
