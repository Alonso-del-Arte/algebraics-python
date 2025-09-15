import random
import unittest

import src.numth
from src.rings import IntegerRing
from src.rings import QuadraticRing

class MockRing(IntegerRing) :
    
    def max_degree(self) :
        return 25

class TestIntegerRing(unittest.TestCase) :
    
    def test_str(self) :
        instance = IntegerRing()
        expected = "Z"
        actual = instance.__str__()
        self.assertEqual(expected, actual)
    
    def test_HTML_str(self) :
        instance = IntegerRing()
        expected = "<b>Z</b>"
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
        
    def test_HTML_blackboardbold_str(self) :
        instance = IntegerRing()
        expectedA = "&#x2124;"
        expectedB = "&#8484;"
        actual = instance.HTML_blackboardbold_str()
        message = actual + " should be " + expectedA + " or " + expectedB
        assert actual == expectedA or actual == expectedB, message
        
    def test_TeX_str(self) :
        instance = IntegerRing()
        expected = "\\textbf Z"
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)
        
    def test_TeX_blackboardbold_str(self) :
        instance = IntegerRing()
        expected = "\\mathbb Z"
        actual = instance.TeX_blackboardbold_str()
        self.assertEqual(expected, actual)
        
    def test_equals(self) :
        expected = IntegerRing()
        actual = IntegerRing()
        self.assertEqual(expected, actual)
        
    def test_not_equals(self) :
        unexpected = IntegerRing()
        actual = MockRing()
        self.assertNotEqual(unexpected, actual)
    
    def test_max_degree(self) :
        instance = IntegerRing()
        expected = 1
        actual = instance.max_degree()
        message = "Reckoning degree of Z"
        self.assertEqual(actual, expected, message)
        
    def test_is_purely_real(self) :
        instance = IntegerRing()
        assert instance.is_purely_real(), "Z is purely real"
        
    def test_discriminant(self) :
        instance = IntegerRing()
        expected = 1
        actual = instance.discriminant()
        message = "Reckoning discriminant of Z"
        self.assertEqual(actual, expected, message)
    
class TestQuadraticRing(unittest.TestCase) :
    
    USUAL_NUMBER_OF_RINGS = 10
    
    def test_str_imag_d_2_mod_4(self) :
        d = -4 * random.randrange(1, 1000) + 2
        rings_so_far = 0
        while rings_so_far < self.USUAL_NUMBER_OF_RINGS :
            if src.numth.squarefree(d) :
                rings_so_far += 1
                instance = QuadraticRing(d)
                expected = f"Z[\u221A\u2212{-d}]"
                actual = instance.__str__()
                self.assertEqual(actual, expected)
            d -= 4
        
if __name__ == '__main__' :
    unittest.main()
