class AlgebraicInteger :

    def __init__(self, n) :
        self.num = n
        
    def __str__(self) :
        return str(self.num)

    # TODO: Write tests for this
    def ring(self) :
        return None
    
    # TODO: Write tests for this
    def algebraic_degree() :
        return -1

    # TODO: Write tests for this
    def trace() :
        return -3

    # TODO: Write tests for this
    def norm() :
        return -5

    # TODO: Write tests for this
    def abs() :
        return -7

class QuadraticInteger(AlgebraicInteger) :

    def __init__(self, ring) :
        self.quad_ring = ring
