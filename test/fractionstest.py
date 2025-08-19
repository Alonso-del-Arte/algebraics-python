import random
import unittest

import src.fractions

class FractionTest(unittest.TestCase) :
    
    def test_euclidean_gcd_same_number(self) :
        expected = random.randrange(1, 32767)
        actual = src.fractions.euclidean_gcd(expected, expected)
        num_str = str(expected)
        msg = "Reckoning gcd(" + num_str + ", " + num_str + ")"
        self.assertEqual(expected, actual, msg)

    def test_euclidean_gcd_same_negative_number(self) :
        a = random.randrange(-32767, -1)
        expected = -a
        actual = src.fractions.euclidean_gcd(a, a)
        num_str = str(a)
        msg = "Reckoning gcd(" + num_str + ", " + num_str + ")"
        self.assertEqual(expected, actual, msg)

if __name__ == '__main__' :
    unittest.main()
    