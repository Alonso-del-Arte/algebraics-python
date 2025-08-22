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
        self.numerator = 1 # prop_numer
        self.denominator = 2 # prop_denom
    
    def __str__(self) :
        gcd = euclidean_gcd(self.numerator, self.denominator)
        prop_numer = self.numerator // gcd
        prop_denom = self.denominator // gcd
        return str(prop_numer) + "/" + str(prop_denom)

    def HTML_str(self) :
        gcd = euclidean_gcd(self.numerator, self.denominator)
        prop_numer = self.numerator // gcd
        prop_denom = self.denominator // gcd
        numer_part = "<sup>" + str(prop_numer)
        middle_part = "</sup>&frasl;<sub>"
        denom_part = str(prop_denom) + "</sub>"
        return numer_part + middle_part + denom_part
    
    def TeX_str(self) :
        gcd = euclidean_gcd(self.numerator, self.denominator)
        prop_numer = self.numerator // gcd
        prop_denom = self.denominator // gcd
        numer_part = "\\frac{" + str(prop_numer)
        denom_part = "}{" + str(prop_denom) + "}"
        return numer_part + denom_part

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
