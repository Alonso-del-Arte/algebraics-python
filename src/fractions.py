def euclidean_gcd(a, b) :
    while b != 0 :
        tempB = b
        b = a % b
        a = tempB
    return abs(a)

class Fraction :
    
    # TODO: Write tests for this
    def __init__(self, numer, denom) :
        self.numerator = numer
        self.denominator = numer
    
    def __str__(self) :
        return str(self.numerator) + "/" + str(self.denominator)

    # TODO: Write tests for this
    def HTML_str(self) :
        return "SORRY, NOT IMPLEMENTED YET"
    
    # TODO: Write tests for this
    def TeX_str(self) :
        return "SORRY, NOT IMPLEMENTED YET"

    # TODO: Write tests for this
    def __add__(self, addend) :
        return self

    # TODO: Write tests for this
    def __neg__(self, divisor) :
        return self

    # TODO: Write tests for this
    def __sub__(self, subtrahend) :
        return self

    # TODO: Write tests for this
    def __mul__(self, multiplicand) :
        return self

    # TODO: Write tests for this
    def __floordiv__(self, divisor) :
        return self
