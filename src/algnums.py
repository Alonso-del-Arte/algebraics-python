from src.rings import IntegerRing

class AlgebraicInteger :

    def __init__(self, n) :
        self.num = n
        
    def __str__(self) :
        return str(self.num)

    def ring(self) :
        return IntegerRing()
    
    # TODO: Write tests for this
    def algebraic_degree(self) :
        return -1

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
