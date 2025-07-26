import random
import unittest

from src.algnums import AlgebraicInteger

class AlgebraicIntegerTest(unittest.TestCase) :
    
    def test_str(self) :
        n = random.randrange(-32768, 32767)
        instance = AlgebraicInteger(n)
        expected = str(n)
        actual = instance.__str__()
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
