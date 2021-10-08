import unittest

from master import add


class CalcTester(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(4, 5), 9)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-4, -5), -9)


if __name__ == '__main__':
    unittest.main()
