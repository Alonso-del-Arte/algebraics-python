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
    
    def test_euclidean_gcd(self) :
        expected = 2 * random.randrange(3, 65535) + 1
        a = 2 * expected
        b = expected * (expected + 2)
        actual = src.fractions.euclidean_gcd(a, b)
        msg = "Reckoning gcd(" + str(a) + ", " + str(b) + ")"
        self.assertEqual(expected, actual, msg)
    
    def test_constructor_sets_numerator(self) :
        expected = random.randrange(1, 1024)
        denom = 2 * expected + 1
        instance = src.fractions.Fraction(expected, denom)
        actual = instance.numerator
        self.assertEqual(expected, actual)
    
    def test_constructor_sets_denominator(self) :
        numer = random.randrange(1, 1024)
        expected = 2 * numer + 1
        instance = src.fractions.Fraction(numer, expected)
        actual = instance.denominator
        self.assertEqual(expected, actual)
    
    def test_str(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(numer, denom)
        expected = str(numer) + "/" + str(denom)
        actual = instance.__str__()
        self.assertEqual(expected, actual)
    
    def test_str_when_constructor_not_get_lowest_terms(self) :
        exp_numer = 2 * random.randrange(1, 2048) + 1
        exp_denom = 2 * exp_numer + 1
        power = 2 ** random.randrange(2, 16)
        multiplier = power * exp_numer * exp_denom
        numer = multiplier * exp_numer
        denom = multiplier * exp_denom
        instance = src.fractions.Fraction(numer, denom)
        expected = str(exp_numer) + "/" + str(exp_denom)
        actual = instance.__str__()
        self.assertEqual(expected, actual)

    def test_HTML_str(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(numer, denom)
        middle_part = "</sup>&frasl;<sub>"
        expected = "<sup>" + str(numer) + middle_part + str(denom) + "<sub>"
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
    
if __name__ == '__main__' :
    unittest.main()
    