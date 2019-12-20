class NonpositiveIntegerException(Exception):
    pass

class IntegerProperties:
    def __init__(self):
        self.visuals = True

    def integer_division(self, x: int, y: int):
        """Preforms floor division"""
        return x//y

    def modular_division(self, x: int, y: int):
        """Preforms modular division"""
        return x % y

    def euclids_algorithm(self, larger: int, smaller: int):
        """Finds the greatest common denomentor using Euclid's Algorithm
            positive integers only"""

        if larger <= 0 or smaller <= 0:
            raise NonpositiveIntegerException

        if smaller > larger:
            temp = larger
            larger = smaller
            smaller = temp

        r = larger % smaller

        if self.visuals == True:
            print("%d / %d = %d R %d" % (larger, smaller, larger // smaller,  r))

        while r != 0:
            larger = smaller
            smaller = r
            r = larger % smaller
            if self.visuals == True:
                print("%d / %d = %d R %d" % (larger, smaller, larger // smaller, r))

        return smaller
