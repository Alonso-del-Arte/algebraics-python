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
        if self.denominator == 1 :
            return str(self.numerator)
        if self.numerator < 0 :
            abs_display = str(abs(self.numerator))
            return "\u2212" + abs_display + "/" + str(self.denominator)
        return str(self.numerator) + "/" + str(self.denominator)

    def HTML_str(self) :
        if self.denominator == 1 :
            return str(self.numerator)
        if self.numerator < 0 :
            numer_part = "&minus;<sup>" + str(abs(self.numerator))
            middle_part = "</sup>&frasl;<sub>"
            denom_part = str(self.denominator) + "</sub>"
            return numer_part + middle_part + denom_part
        numer_part = "<sup>" + str(self.numerator)
        middle_part = "</sup>&frasl;<sub>"
        denom_part = str(self.denominator) + "</sub>"
        return numer_part + middle_part + denom_part
    
    def TeX_str(self) :
        if self.denominator == 1 :
            return str(self.numerator)
        if self.numerator < 0 :
            return "\\frac{" + str(self.numerator) + "}{" + str(self.denominator) + "}"
        numer_part = "\\frac{" + str(self.numerator)
        denom_part = "}{" + str(self.denominator) + "}"
        return numer_part + denom_part

    def __eq__(self, other) :
        match_numer = self.numerator == other.numerator
        return match_numer and self.denominator == other.denominator
    
    def __add__(self, addend) :
        cross_multA = self.numerator * addend.denominator
        cross_multB = addend.numerator * self.denominator
        numer = cross_multA + cross_multB
        denom = self.denominator * addend.denominator
        return Fraction(numer, denom)

    def __neg__(self) :
        return Fraction(-self.numerator, self.denominator)

    def __sub__(self, subtrahend) :
        cross_multA = self.numerator * subtrahend.denominator
        cross_multB = subtrahend.numerator * self.denominator
        numer = cross_multA - cross_multB
        denom = self.denominator * subtrahend.denominator
        return Fraction(numer, denom)

    # TODO: Write tests for this
    def __mul__(self, multiplicand) :
        return self

    # TODO: Write tests for this
    def reciprocal(self) :
        return self

    # TODO: Write tests for this
    def __truediv__(self, divisor) :
        return self
