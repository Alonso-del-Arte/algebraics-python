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
        return True

    def ring(self) :
        return IntegerRing()
    
    def algebraic_degree(self) :
        if self.num == 0 :
            return 0
        return 1

    # TODO: Write tests for this
    def trace(self) :
        return -3

    # TODO: Write tests for this
    def norm(self) :
        return -5

    def abs(self) :
        return abs(self.num)
    
    # TODO: Write tests for this
    def __add__(self, addend) :
        return self

    # TODO: Write tests for this
    def __sub__(self, subtrahend) :
        return self

    # TODO: Write tests for this
    def __neg__(self, divisor) :
        return self

    # TODO: Write tests for this
    def __mul__(self, multiplicand) :
        return self

    # TODO: Write tests for this
    def __floordiv__(self, divisor) :
        return self

    # TODO: Write tests for this
    def __mod__(self, divisor) :
        return self

class QuadraticInteger(AlgebraicInteger) :

    def __init__(self, a, b, ring) :
        self.quad_ring = ring
