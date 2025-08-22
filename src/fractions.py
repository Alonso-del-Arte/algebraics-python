def euclidean_gcd(a, b) :
    while b != 0 :
        tempB = b
        b = a % b
        a = tempB
    return abs(a)

class Fraction :
    
    def __init__(self, numer, denom) :
        self.numerator = numer
        self.denominator = denom
    
    def __str__(self) :
        gcd = euclidean_gcd(self.numerator, self.denominator)
        prop_numer = self.numerator // gcd
        prop_denom = self.denominator // gcd
        return str(prop_numer) + "/" + str(prop_denom)

    # TODO: Write tests for this
    def HTML_str(self) :
        numer_part = "<sup>" + str(self.numerator)
        middle_part = "</sup>&frasl;<sub>"
        denom_part = str(self.denominator) + "</sub>"
        return numer_part + middle_part + denom_part
    
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
