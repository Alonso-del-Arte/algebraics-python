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
        expected = "<sup>" + str(numer) + middle_part + str(denom) + "</sub>"
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
    
    def test_HTML_str_when_constructor_not_get_lowest_terms(self) :
        exp_numer = 2 * random.randrange(1, 2048) + 1
        exp_denom = 2 * exp_numer + 1
        power = 2 ** random.randrange(2, 16)
        multiplier = power * exp_numer * exp_denom
        numer = multiplier * exp_numer
        denom = multiplier * exp_denom
        instance = src.fractions.Fraction(numer, denom)
        numer_part = "<sup>" + str(exp_numer)
        middle_part = "</sup>&frasl;<sub>"
        denom_part = str(exp_denom) + "</sub>"
        expected = numer_part + middle_part + denom_part
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)

    def test_TeX_str(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(numer, denom)
        expected = "\\frac{" + str(numer) + "}{" + str(denom) + "}"
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)
    
    def test_TeX_str_when_constructor_not_get_lowest_terms(self) :
        exp_numer = 2 * random.randrange(1, 2048) + 1
        exp_denom = 2 * exp_numer + 1
        power = 2 ** random.randrange(2, 16)
        multiplier = power * exp_numer * exp_denom
        numer = multiplier * exp_numer
        denom = multiplier * exp_denom
        instance = src.fractions.Fraction(numer, denom)
        expected = "\\frac{" + str(exp_numer) + "}{" + str(exp_denom) + "}"
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)

    def test_constructor_sets_numerator_from_not_lowest_terms(self) :
        expected = random.randrange(1, 1024)
        denom = 3 * expected + 1 + (expected % 2)
        power = 5 ** random.randrange(2, 10)
        multiplier = power * expected * denom
        show_numer = multiplier * expected
        show_denom = multiplier * denom
        instance = src.fractions.Fraction(show_numer, show_denom)
        actual = instance.numerator
        message = "Fraction is " + str(expected) + "/" + str(denom)
        self.assertEqual(expected, actual, message)
    
    def test_constructor_sets_denominator_from_not_lowest_terms(self) :
        numer = random.randrange(1, 1024)
        expected = 5 * numer + 1 + (numer % 2)
        power = 3 ** random.randrange(2, 12)
        multiplier = power * numer * expected
        show_numer = multiplier * numer
        show_denom = multiplier * expected
        instance = src.fractions.Fraction(show_numer, show_denom)
        actual = instance.denominator
        message = "Fraction is " + str(numer) + "/" + str(expected)
        self.assertEqual(expected, actual, message)
    
if __name__ == '__main__' :
    unittest.main()
