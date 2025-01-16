import unittest

from src.addition_test import adding_two_positive_numbers

class test_adding_two_numbers(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(adding_two_positive_numbers(3,6), 10)

if __name__ == '__main__':
    unittest.main()    