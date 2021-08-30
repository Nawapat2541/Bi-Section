class Polynomial:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        self.coefficients = list(coefficients) # tuple is turned into a list

    # The __repr__ and __str__ method can be included here,
    # but is not necessary for the immediately following code

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x** index
        return res


class Polynomial2:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        self.coefficients = list(coefficients) # tuple is turned into a list

    # The __repr__ and __str__ method can be included here,
    # but is not necessary for the immediately following code

    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res