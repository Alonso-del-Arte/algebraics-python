class IntegerRing :
    
    def __init__(self) :
        pass
    
    def __str__(self) :
        return "Z"
    
    # TODO: Write tests for this
    def HTMLstr(self) :
        return self.__str__()
    
    # TODO: Write tests for this
    def TeXstr(self) :
        return self.__str__()
    
    def __eq__(self, other) :
        return type(self) == type(other) and other.max_degree() == 1
    
    def max_degree(self) :
        return 1
    
    def is_purely_real(self) :
        return True
    
    def discriminant(self) :
        return 1

class QuadraticRing(IntegerRing) :

    def __init__(self, d) :
        print('PLACEHOLDER 2')
