class IntegerRing :
    
    def __str__(self) :
        return "Z"
    
    def __eq__(self, other) :
        return True
    
    def max_degree(self) :
        return 1
    
    def is_purely_real(self) :
        return True
    
    def discriminant(self) :
        return 1

class QuadraticRing(IntegerRing) :

    def __init__(self, d) :
        print('PLACEHOLDER 2')
