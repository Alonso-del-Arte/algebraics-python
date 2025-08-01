import random
import unittest

from src.algnums import AlgebraicInteger
from src.rings import IntegerRing

class AlgebraicIntegerTest(unittest.TestCase) :
    
    def test_str(self) :
        n = random.randrange(-32768, 32767)
        instance = AlgebraicInteger(n)
        expected = str(n)
        actual = instance.__str__()
        self.assertEqual(expected, actual)
        
    def test_HTML_str_positive(self) :
        n = random.randrange(0, 32767)
        instance = AlgebraicInteger(n)
        expected = str(n)
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
        
    def test_HTML_str(self) :
        n = random.randrange(1, 32768)
        instance = AlgebraicInteger(-n)
        expected = "&minus;" + str(n)
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
        
    def test_TeX_str(self) :
        n = random.randrange(-32768, 32767)
        instance = AlgebraicInteger(n)
        expected = str(n)
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)
        
    def test_ring(self) :
        n = random.randrange(-32768, 32767)
        instance = AlgebraicInteger(n)
        expected = IntegerRing()
        actual = instance.ring()
        self.assertEqual(expected, actual)
        
    def test_abs_already_positive(self) :
        expected = random.randrange(1, 65536)
        instance = AlgebraicInteger(expected)
        actual = instance.abs()
        self.assertEqual(expected, actual)
        
    def test_abs(self) :
        n = -random.randrange(1, 65536)
        instance = AlgebraicInteger(n)
        expected = abs(n)
        actual = instance.abs()
        self.assertEqual(expected, actual)

if __name__ == '__main__' :
    unittest.main()
