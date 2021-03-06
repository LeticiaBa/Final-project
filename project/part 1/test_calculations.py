import unittest

from calculations import *


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(one(3), 6)
        with self.assertRaises(ValueError):
            one(-1)
            one('f')
            one(3.5)
            one(0)

    def test_two(self):
        self.assertEqual(two(2, 3), 8)
        with self.assertRaises(ValueError):
            two(-1, 1)
            two(1, -1)
            two(-1, -1)
            two(0, 4)
            two(4, 0)
            two(0, 0)
            two(3.5, 1)
            two(1, 3.5)
            two(1.5, 3.5)

    def test_three(self):
        self.assertEqual(three(7), '7 6 5 4 3 2 1')
        with self.assertRaises(ValueError):
            three(-1)
            three(3.5)
            three(0)


if __name__ == '__main__':
    unittest.main()
