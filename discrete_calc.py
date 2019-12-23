import collections
import re

InverseEquation = collections.namedtuple("InverseEquation", "value coefficient1 constant1 coefficient2 constant2")


class NonpositiveIntegerException(Exception):
    pass


class NoInverseException(Exception):
    pass


class InvalidBaseException(Exception):
    pass


class InvalidNumException(Exception):
    pass

class IntegerProperties:
    def __init__(self):
        self.visuals = False
        self.inverse_equations = []

    def integer_division(self, x: int, y: int):
        """Preforms floor division"""
        return x//y

    def modular_division(self, x: int, y: int):
        """Preforms modular division"""
        return x % y

    def euclids_algorithm(self, larger: int, smaller: int):
        """Finds the greatest common denominator using Euclid's Algorithm
            positive integers only"""

        if larger <= 0 or smaller <= 0:
            raise NonpositiveIntegerException

        self.inverse_equations.clear()

        if smaller > larger:
            temp = larger
            larger = smaller
            smaller = temp

        r = larger % smaller

        if self.visuals == True:
            print("%d / %d = %d R %d" % (larger, smaller, larger // smaller,  r))

        self.inverse_equations.insert(0, InverseEquation(value=r, coefficient1=1, constant1=larger, coefficient2=
                                                     -1 * (larger//smaller), constant2=smaller))
        while r != 0:
            larger = smaller
            smaller = r
            r = larger % smaller
            if self.visuals == True:
                print("%d / %d = %d R %d" % (larger, smaller, larger // smaller, r))
            if r != 0:
                self.inverse_equations.insert(0, InverseEquation(value=r, coefficient1=1, constant1=larger, coefficient2
                                                                =-1 * (larger//smaller), constant2=smaller))

        return smaller

    def inverse(self, x: int, n: int):
        """sx mod n, finding s"""

        if self.euclids_algorithm(x, n) != 1:
            raise NoInverseException

        main_inverse_equation = {
            "value": self.inverse_equations[0].value,
            "coefficient1": self.inverse_equations[0].coefficient1,
            "constant1": self.inverse_equations[0].constant1,
            "substituted_coefficient": 1,
            "substituted_constant": 0,
            "coefficient2": self.inverse_equations[0].coefficient2,
            "constant2": self.inverse_equations[0].constant2,
        }
        if self.visuals == True:
            print("%d = (%d)%d + (%d)%d" % (
                main_inverse_equation["value"], main_inverse_equation["coefficient1"],
                main_inverse_equation["constant1"], main_inverse_equation["coefficient2"],
                main_inverse_equation["constant2"]
            ))

        for i_equation in self.inverse_equations[1:]:
            main_inverse_equation["substituted_constant"] = i_equation.constant1
            main_inverse_equation["constant2"] = i_equation.constant2

            multiplying_sub = main_inverse_equation["coefficient2"]

            main_inverse_equation["coefficient2"] = i_equation.coefficient2
            main_inverse_equation["substituted_coefficient"] *= multiplying_sub
            main_inverse_equation["coefficient2"] *= multiplying_sub
            main_inverse_equation["coefficient2"] += main_inverse_equation["coefficient1"]

            main_inverse_equation["coefficient1"] = main_inverse_equation["substituted_coefficient"]
            main_inverse_equation["constant1"] = main_inverse_equation["substituted_constant"]

            main_inverse_equation["substituted_coefficient"] = 1
            main_inverse_equation["substituted_constant"] = 0
            if self.visuals == True:
                print("%d = (%d)%d + (%d)%d" % (
                    main_inverse_equation["value"], main_inverse_equation["coefficient1"],
                    main_inverse_equation["constant1"], main_inverse_equation["coefficient2"],
                    main_inverse_equation["constant2"]
                ))

        if main_inverse_equation["constant1"] == x:
            return self.modular_division(main_inverse_equation["coefficient1"], n)

        elif main_inverse_equation["constant2"] == x:
            return self.modular_division(main_inverse_equation["coefficient2"], n)

        else:
            return 0

    def base_to_deci(self, num: str, base: int):
        """Takes a non-negative base number from 1-16 and turns it into its decimal representation"""

        numberdict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        new_num = 0
        exponent = len(num) - 1
        if base <= 0 or base > 16:
            raise InvalidBaseException

        pattern = re.compile(r"(^[(0-9)ABCDEF]+$)")

        if re.match(pattern, num) == None:
            raise InvalidNumException

        for value in num:
            if value in numberdict:
                if numberdict[value] > base:
                    raise InvalidNumException
                new_num += (numberdict[value] * (base**exponent))
            elif int(value) > base:
                raise InvalidNumException
            else:
                new_num += (int(value) * (base ** exponent))
            exponent -= 1
        return new_num

    def deci_to_base(self, num: int, base: int):
        """Takes a non-negative base number from 1-16 and turns it into its decimal representation"""
        if base <= 0 or base > 16:
            raise InvalidBaseException
        letterdict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

        new_deci_num = ""

        while num != 0:
            if num % base in letterdict:
                new_deci_num += letterdict[num % base]
            else:
                new_deci_num += str(num % base)
            num = num // base

        return new_deci_num[::-1]

    def fast_expo(self, base: int, exponent: int, mod: int):
        """Preforms fast modular exponentiation"""

        if base <= 0 or exponent <= 0 or mod <= 0:
            raise NonpositiveIntegerException

        partial = 1
        current = base
        expansion = exponent

        while expansion > 0:
            if expansion % 2 == 1:
                partial *= (current % mod)
            current *= (current % mod)
            expansion = expansion // 2

        return partial % mod









