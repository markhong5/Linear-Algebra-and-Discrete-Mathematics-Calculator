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

    def test_base_to_deci(self):
        self.assertRaises(InvalidBaseException, self.discrete_object.base_to_deci, "123", 0)
        self.assertRaises(InvalidBaseException, self.discrete_object.base_to_deci, "123", -1)
        self.assertRaises(InvalidBaseException, self.discrete_object.base_to_deci, "123", 17)
        self.assertRaises(InvalidNumException, self.discrete_object.base_to_deci, "578.1", 10)
        self.assertRaises(InvalidNumException, self.discrete_object.base_to_deci, "ABC", 3)
        self.assertRaises(InvalidNumException, self.discrete_object.base_to_deci, "ABC", 10)

        self.assertEqual(self.discrete_object.base_to_deci("1100110", 2), 102)
        self.assertEqual(self.discrete_object.base_to_deci("346", 7), 181)
        self.assertEqual(self.discrete_object.base_to_deci("3B2", 16), 946)
        self.assertEqual(self.discrete_object.base_to_deci("120121", 3), 421)
        self.assertEqual(self.discrete_object.base_to_deci("A22", 11), 1234)
        self.assertEqual(self.discrete_object.base_to_deci("50020", 8), 20496)

    def test_deci_to_base(self):
        self.assertRaises(InvalidBaseException, self.discrete_object.base_to_deci, "123", 0)
        self.assertRaises(InvalidBaseException, self.discrete_object.base_to_deci, "123", -1)
        self.assertEqual(self.discrete_object.deci_to_base(217, 2), "11011001")
        self.assertEqual(self.discrete_object.deci_to_base(344, 16), "158")
        self.assertEqual(self.discrete_object.deci_to_base(136, 7), "253")
        self.assertEqual(self.discrete_object.deci_to_base(542, 5), "4132")
        self.assertEqual(self.discrete_object.deci_to_base(171, 16), "AB")
        self.assertEqual(self.discrete_object.deci_to_base(91, 3), "10101")

    def test_fast_mod_exponent(self):
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.fast_expo, -1, 3, 0)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.fast_expo, 1, -3, 0)
        self.assertRaises(NonpositiveIntegerException, self.discrete_object.fast_expo, 1, 3, -5)
        self.assertEqual(self.discrete_object.fast_expo(5, 35, 11), 1)
        self.assertEqual(self.discrete_object.fast_expo(5, 68, 7), 4)
        self.assertEqual(self.discrete_object.fast_expo(53, 27, 12), 5)
        self.assertEqual(self.discrete_object.fast_expo(46, 39, 11), 6)
        self.assertEqual(self.discrete_object.fast_expo(4, 74, 13), 3)




if __name__ == '__main__':
    unittest.main()