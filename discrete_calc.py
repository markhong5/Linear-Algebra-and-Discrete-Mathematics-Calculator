import collections

InverseEquation = collections.namedtuple("InverseEquation", "value coefficient1 constant1 coefficient2 constant2")

class NonpositiveIntegerException(Exception):
    pass

class NoInverseException(Exception):
    pass

class IntegerProperties:
    def __init__(self):
        self.visuals = True
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



