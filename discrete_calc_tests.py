import unittest
from discrete_calc import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.discrete_object = IntegerProperties()

    def test_modular_and_division(self):
        self.assertEqual(self.discrete_object.integer_division(21, 4), 5)
        self.assertEqual(self.discrete_object.integer_division(-21, 4), -6)

        self.assertEqual(self.discrete_object.modular_division(47, 11), 3)
        self.assertEqual(self.discrete_object.modular_division(-47, 11), 8)

    def test_euclids_algorithm(self):

        self.assertEqual(self.discrete_object.euclids_algorithm(31, 198), 1)
        self.assertEqual(self.discrete_object.euclids_algorithm(42, 9000), 6)

        self.assertEqual(self.discrete_object.euclids_algorithm(453, 3), 3)
        self.assertEqual(self.discrete_object.euclids_algorithm(630, 147), 21)

        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, 0, 95)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, 95, 0)

        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, 31, -198)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, 198, -31)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, -31, -198)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, -198, -31)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, -31, 198)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.euclids_algorithm, -198, 31)

    def test_multiplicative_inverse(self):

        self.assertEqual(self.discrete_object.inverse(77, 52), 25)
        self.assertEqual(self.discrete_object.inverse(53, 71), 67)

        self.assertEqual(self.discrete_object.inverse(71, 53), 3)
        self.assertEqual(self.discrete_object.inverse(34, 55), 34)
        self.assertEqual(self.discrete_object.inverse(55, 34), 13)

        self.assertEqual(self.discrete_object.inverse(61, 54), 31)
        self.assertEqual(self.discrete_object.inverse(54, 61), 26)

        self.assertRaises(NoInverseException, self.discrete_object.inverse, 453, 3)
        self.assertRaises(NoInverseException, self.discrete_object.inverse, 147, 630)




if __name__ == '__main__':
    unittest.main()