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
        # TODO: Refactor
        if self.radicand == -3 :
            return "Z[\u03C9]"
        if self.radicand == -1 :
            return "Z[i]"
        if self.radicand == 5 :
            return "Z[\u03C6]"
        if self.radicand % 4 == 3 :
            if self.radicand < 0 :
                return f"Z[\u221A\u2212{-self.radicand}]"
            return f"Z[\u221A{self.radicand}]"
        if self.radicand > 0 and self.radicand % 4 == 1 :
            return f"O_Q(\u221A{self.radicand})"
        if self.radicand > 0 :
            return f"Z[\u221A{self.radicand}]"
        if self.radicand < 0 and self.radicand % 4 == 1 :
            return f"O_Q(\u221A\u2212{-self.radicand})"
        return f"Z[\u221A\u2212{-self.radicand}]"
    
    def TeX_str(self) :
        if self.radicand == -3 :
            return "\\textbf Z[\\omega]"
        if self.radicand == -1 :
            return "\\textbf Z[i]"
        if self.radicand == 5 :
            return "\\textbf Z[\\phi]"
        if self.radicand % 4 == 1 :
            return "\\mathcal O_{\\textbf Q(\\sqrt{" + str(self.radicand) + "})}"
        return "\\textbf Z[\\sqrt{" + str(self.radicand) + "}]"

    def TeX_blackboardbold_str(self) :
        if self.radicand % 4 == 2 :
            return "\\mathbb Z[\\sqrt{" + str(self.radicand) + "}]"
        if self.radicand == -1 :
            return "\\mathbb Z[i]"
        if self.radicand % 4 == 3 :
            return "\\mathbb Z[\\sqrt{" + str(self.radicand) + "}]"
        if self.radicand == -3 :
            return "\\mathbb Z[\\omega]"
        if self.radicand == 5 :
            return "\\mathbb Z[\\phi]"
        return "\\mathcal O_{\\mathbb Q(\\sqrt{" + str(self.radicand) + "})}"
    
    def HTML_str(self) :
        if self.radicand == -3 :
            return "<b>Z</b>[&omega;]"
        return f"<i>O</i><sub><b>Q</b>(&radic;&minus;{-self.radicand})</sub>"
    