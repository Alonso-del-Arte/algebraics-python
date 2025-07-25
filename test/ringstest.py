import unittest
from src.rings import IntegerRing

class TestIntegerRing(unittest.TestCase) :
    
    def test_max_degree(self) :
        instance = IntegerRing()
        expected = 1
        actual = instance.max_degree()
        message = "Reckoning degree of Z"
        self.assertEqual(actual, expected, message)
        
if __name__ == '__main__' :
    unittest.main()
