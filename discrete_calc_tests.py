import unittest
from discrete_calc import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.discrete_object = Integer_properties()

    def test_modular_and_division(self):
        self.assertEqual(self.discrete_object.integer_division(21, 4), 5)
        self.assertEqual(self.discrete_object.integer_division(-21, 4), -6)

        self.assertEqual(self.discrete_object.modular_division(47, 11), 3)
        self.assertEqual(self.discrete_object.modular_division(-47, 11), 8)




if __name__ == '__main__':
    unittest.main()