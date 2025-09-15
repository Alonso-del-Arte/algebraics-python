class IntegerRing :
    
    def __init__(self) :
        pass
    
    def __str__(self) :
        return "Z"
    
    def HTML_str(self) :
        return "<b>Z</b>"
    
    def HTML_blackboardbold_str(self) :
        return "&#x2124;"
    
    def TeX_str(self) :
        return "\\textbf Z"
    
    def TeX_blackboardbold_str(self) :
        return "\\mathbb Z"
    
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
        self.radicand = d
    
    def __str__(self) :
        if self.radicand > 0 :
            return f"Z[\u221A{self.radicand}]"
        return f"Z[\u221A\u2212{-self.radicand}]"
