def euclidean_gcd(a, b) :
    while b != 0 :
        tempB = b
        b = a % b
        a = tempB
    return abs(a)

# TODO: Assess whether this class is even necessary, given the Fraction class in 
# the Python standard library
class Fraction :
    
    def __init__(self, numer, denom) :
        gcd = euclidean_gcd(numer, denom)
        prop_numer = numer // gcd
        prop_denom = denom // gcd
        self.numerator = prop_numer
        self.denominator = prop_denom
    
    def __str__(self) :
        return str(self.numerator) + "/" + str(self.denominator)

    def HTML_str(self) :
        numer_part = "<sup>" + str(self.numerator)
        middle_part = "</sup>&frasl;<sub>"
        denom_part = str(self.denominator) + "</sub>"
        return numer_part + middle_part + denom_part
    
    def TeX_str(self) :
        numer_part = "\\frac{" + str(self.numerator)
        denom_part = "}{" + str(self.denominator) + "}"
        return numer_part + denom_part

    def __eq__(self, other) :
        match_numer = self.numerator == other.numerator
        return match_numer and self.denominator == other.denominator
    
    # TODO: Write tests for this
    def __add__(self, addend) :
        return Fraction(self.numerator - addend.numerator, self.denominator)

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
    def __truediv__(self, divisor) :
        return self
