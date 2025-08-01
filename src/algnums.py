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

class QuadraticInteger(AlgebraicInteger) :

    def __init__(self, ring) :
        self.quad_ring = ring
