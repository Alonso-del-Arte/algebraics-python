from src.rings import IntegerRing

class AlgebraicInteger :

    def __init__(self, n) :
        self.num = n
        
    def __str__(self) :
        return str(self.num)
    
    def HTML_str(self) :
        if self.num < 0 :
            return "&minus;" + str(-self.num)
        return str(self.num)
    
    def TeX_str(self) :
        return self.__str__()
    
    def __eq__(self, other) :
        return self.num == other.num

    def ring(self) :
        return IntegerRing()
    
    def algebraic_degree(self) :
        if self.num == 0 :
            return 0
        return 1

    def trace(self) :
        return self.num

    def norm(self) :
        return self.num

    def abs(self) :
        return abs(self.num)
    
    def __add__(self, addend) :
        return AlgebraicInteger(self.num + addend.num)

    def __sub__(self, subtrahend) :
        return AlgebraicInteger(self.num - subtrahend.num)

    def __neg__(self) :
        return AlgebraicInteger(-self.num)

    def __mul__(self, multiplicand) :
        return AlgebraicInteger(self.num * multiplicand.num)

    # TODO: Write tests for this
    def __floordiv__(self, divisor) :
        return self

    # TODO: Write tests for this
    def __mod__(self, divisor) :
        return self

class QuadraticInteger(AlgebraicInteger) :

    def __init__(self, a, b, ring) :
        self.quad_ring = ring
