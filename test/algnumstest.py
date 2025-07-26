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

if __name__ == '__main__' :
    unittest.main()
