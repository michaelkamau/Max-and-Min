import unittest
from max_min_src.max_min import find_max_min


class MaxMinTest(unittest.TestCase):
    """docstring for MaxMinTest"""

    def test_find_max_min_four(self):
        self.assertListEqual([1, 4],
                             find_max_min([1, 2, 3, 4]),
                             msg='should return [1,4] for [1, 2, 3, 4]')

    def test_find_max_min_one(self):
        self.assertListEqual([4, 6],
                             find_max_min([6, 4]),
                             msg='should return [4, 6] for [6, 4]')