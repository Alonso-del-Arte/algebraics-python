import unittest
from src.rings import IntegerRing

class TestIntegerRing(unittest.TestCase) :
    
    def test_str(self) :
        instance = IntegerRing()
        expected = "Z"
        actual = instance.__str__()
        self.assertEqual(expected, actual)
    
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
        
if __name__ == '__main__' :
    unittest.main()
