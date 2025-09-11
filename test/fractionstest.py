import random
import unittest

import src.fractions

class FractionTest(unittest.TestCase) :
    
    SOME_PRIMES = [277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
                   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
                   431, 433, 439, 443, 449]
    
    NUMBER_OF_PRIMES = len(SOME_PRIMES)
    
    def test_euclidean_gcd_same_number(self) :
        expected = random.randrange(1, 32767)
        actual = src.fractions.euclidean_gcd(expected, expected)
        msg = f"Reckoning gcd({expected}, {expected})"
        self.assertEqual(expected, actual, msg)

    def test_euclidean_gcd_same_negative_number(self) :
        a = random.randrange(-32767, -1)
        expected = -a
        actual = src.fractions.euclidean_gcd(a, a)
        num_str = str(a)
        msg = f"Reckoning gcd({a}, {a})"
        self.assertEqual(expected, actual, msg)
    
    def test_euclidean_gcd(self) :
        expected = 2 * random.randrange(3, 65535) + 1
        a = 2 * expected
        b = expected * (expected + 2)
        actual = src.fractions.euclidean_gcd(a, b)
        msg = f"Reckoning gcd({a}, {b})"
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
        expected = f"{numer}/{denom}"
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
        expected = f"{exp_numer}/{exp_denom}"
        actual = instance.__str__()
        self.assertEqual(expected, actual)

    def test_HTML_str(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(numer, denom)
        expected = f"<sup>{numer}</sup>&frasl;<sub>{denom}</sub>"
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
        expected = f"<sup>{exp_numer}</sup>&frasl;<sub>{exp_denom}</sub>"
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
    
    def test_str_positive_integer(self) :
        numer = random.randrange(1, 4096)
        instance = src.fractions.Fraction(numer, 1)
        expected = str(numer)
        actual = str(instance)
        self.assertEqual(expected, actual)

    def test_HTML_str_positive_integer(self) :
        numer = random.randrange(1, 4096)
        instance = src.fractions.Fraction(numer, 1)
        expected = str(numer)
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)

    def test_TeX_str_positive_integer(self) :
        numer = random.randrange(1, 4096)
        instance = src.fractions.Fraction(numer, 1)
        expected = str(numer)
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)

    def test_str_negative(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(-numer, denom)
        expected = f"\u2212{numer}/{denom}"
        actual = instance.__str__()
        self.assertEqual(expected, actual)
    
    def test_HTML_str_negative(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(-numer, denom)
        expected = f"&minus;<sup>{numer}</sup>&frasl;<sub>{denom}</sub>"
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
    
    def test_TeX_str_negative(self) :
        numer = random.randrange(1, 32767)
        denom = numer + 1
        instance = src.fractions.Fraction(-numer, denom)
        expected = "-\\frac{" + str(numer) + "}{" + str(denom) + "}"
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)
    
    def test_str_negative_integer(self) :
        numer = random.randrange(1, 32767)
        instance = src.fractions.Fraction(-numer, 1)
        expected = f"\u2212{numer}"
        actual = instance.__str__()
        self.assertEqual(expected, actual)
    
    def test_HTML_str_negative_integer(self) :
        numer = random.randrange(1, 32767)
        instance = src.fractions.Fraction(-numer, 1)
        expected = f"&minus;{numer}"
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
    
    def test_TeX_str_negative_integer(self) :
        numer = random.randrange(1, 32767)
        instance = src.fractions.Fraction(-numer, 1)
        expected = str(-numer)
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
        message = f"Fraction is {expected}/{denom}"
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
        message = f"Fraction is {numer}/{expected}"
        self.assertEqual(expected, actual, message)
    
    def test_not_equal_diff_numer(self) :
        numerA = random.randrange(1, 512)
        numerB = numerA + random.randrange(1, 511)
        denom = random.randrange(1, 1024)
        fractionA = src.fractions.Fraction(numerA, denom)
        fractionB = src.fractions.Fraction(numerB, denom)
        message = str(fractionA) + " should not equal " + str(fractionB)
        self.assertNotEqual(fractionA, fractionB, message)
    
    def test_eq(self) :
        numer = random.randrange(1, 65536)
        denom = numer + random.randrange(1, 128)
        some_fraction = src.fractions.Fraction(numer, denom)
        same_fraction = src.fractions.Fraction(numer, denom)
        message = str(some_fraction) + " should equal " + str(same_fraction)
        self.assertEqual(some_fraction, same_fraction)
        
    def test_not_equal_diff_denom(self) :
        index = random.randrange(0, self.NUMBER_OF_PRIMES - 1)
        numer = self.SOME_PRIMES[index]
        denomA = random.randrange(numer + 1, 2 * numer - 1)
        denomB = random.randrange(2 * numer + 1, 3 * numer - 1)
        fractionA = src.fractions.Fraction(numer, denomA)
        fractionB = src.fractions.Fraction(numer, denomB)
        message = str(fractionA) + " should not equal " + str(fractionB)
        self.assertNotEqual(fractionA, fractionB, message)
    
    def test_equals_even_if_not_in_lowest_terms(self) :
        index = random.randrange(0, self.NUMBER_OF_PRIMES - 1)
        numer = self.SOME_PRIMES[index]
        denom = random.randrange(1, 256)
        mult = random.randrange(2, 32)
        some_fraction = src.fractions.Fraction(numer, denom)
        same_fraction = src.fractions.Fraction(numer * mult, denom * mult)
        message = str(some_fraction) + " should equal " + str(same_fraction)
        self.assertEqual(some_fraction, same_fraction, message)
    
    def test_add_same_denominator(self) :
        index = random.randrange(0, self.NUMBER_OF_PRIMES - 1)
        denom = self.SOME_PRIMES[index]
        numerA = random.randrange(1, denom - 1)
        numerB = random.randrange(1, denom - numerA - 1)
        addendA = src.fractions.Fraction(numerA, denom)
        addendB = src.fractions.Fraction(numerB, denom)
        expected = src.fractions.Fraction(numerA + numerB, denom)
        actual = addendA + addendB
        msgPart = "Adding up " + addendA.__str__() + " and " + addendB.__str__()
        message = msgPart + " expected " + str(expected) + " got " + str(actual)
        self.assertEqual(expected, actual, message)
    
    def test_add(self) :
        addendA_numer = random.randrange(1, 128)
        addendB_numer = random.randrange(1, 128)
        addendA_denom = random.randrange(2, 128)
        addendB_denom = random.randrange(129, 256)
        addendA = src.fractions.Fraction(addendA_numer, addendA_denom)
        addendB = src.fractions.Fraction(addendB_numer, addendB_denom)
        exp_num = addendA_numer * addendB_denom + addendB_numer * addendA_denom
        exp_den = addendA_denom * addendB_denom
        expected = src.fractions.Fraction(exp_num, exp_den)
        actual = addendA + addendB
        msgPart = "Adding up " + addendA.__str__() + " and " + addendB.__str__()
        message = msgPart + " expected " + str(expected) + " got " + str(actual)
        self.assertEqual(expected, actual, message)
    
    def test_subtract_same_denominator(self) :
        index = random.randrange(0, self.NUMBER_OF_PRIMES - 1)
        denom = self.SOME_PRIMES[index]
        subtrahend_numer = random.randrange(1, denom - 2)
        minuend_numer = random.randrange(subtrahend_numer + 1, denom - 1)
        minuend = src.fractions.Fraction(minuend_numer, denom)
        subtrahend = src.fractions.Fraction(subtrahend_numer, denom)
        numer = minuend_numer - subtrahend_numer
        expected = src.fractions.Fraction(numer, denom)
        actual = minuend - subtrahend
        msgPart = "Subtracting " + str(subtrahend) + " from " + str(minuend)
        message = msgPart + " expected " + str(expected) + " got " + str(actual)
        self.assertEqual(expected, actual, message)
    
    def test_sub(self) :
        minuend_numer = random.randrange(1, 128)
        subtr_numer = random.randrange(1, 128)
        subtr_denom = random.randrange(2, 128)
        minuend_denom = random.randrange(129, 256)
        minuend = src.fractions.Fraction(minuend_numer, minuend_denom)
        subtrahend = src.fractions.Fraction(subtr_numer, subtr_denom)
        exp_num = minuend_numer * subtr_denom - subtr_numer * minuend_denom
        exp_den = minuend_denom * subtr_denom
        expected = src.fractions.Fraction(exp_num, exp_den)
        actual = minuend - subtrahend
        msgPart = "Subtracting " + str(subtrahend) + " from " + str(minuend)
        message = msgPart + " expected " + str(expected) + " got " + str(actual)
        self.assertEqual(expected, actual, message)
    
    def test_neg(self) :
        denom = random.randrange(3, 2048)
        numer = random.randrange(1, denom - 1)
        instance = src.fractions.Fraction(numer, denom)
        expected = src.fractions.Fraction(-numer, denom)
        actual = -instance
        message = str(instance) + " negated should be " + str(expected)
        self.assertEqual(expected, actual, message)
    
    def test_negate_negative(self) :
        denom = random.randrange(3, 2048)
        numer = random.randrange(1, denom - 1)
        instance = src.fractions.Fraction(-numer, denom)
        expected = src.fractions.Fraction(numer, denom)
        actual = -instance
        message = str(instance) + " negated should be " + str(expected)
        self.assertEqual(expected, actual, message)
    
    def test_negate_zero(self) :
        expected = src.fractions.Fraction(0, 1)
        actual = -expected
        message = str(expected) + " negated should be that, got " + str(actual)
        self.assertEqual(expected, actual, message)
    
    def test_mul(self) :
        numerA = random.randrange(1, 65535)
        denomA = random.randrange(2, 65536)
        multiplicandA = src.fractions.Fraction(numerA, denomA)
        numerB = random.randrange(1, 65535)
        denomB = random.randrange(2, 65536)
        multiplicandB = src.fractions.Fraction(numerB, denomB)
        exp_numer = numerA * numerB
        exp_denom = denomA * denomB
        expected = src.fractions.Fraction(exp_numer, exp_denom)
        actual = multiplicandA * multiplicandB
        msgPart = str(multiplicandA) + " times " + str(multiplicandB)
        message = msgPart + " should be " + str(expected)
        self.assertEqual(expected, actual, message)
    
    def test_truediv(self) :
        numerA = random.randrange(1, 65535)
        denomA = random.randrange(2, 65536)
        dividend = src.fractions.Fraction(numerA, denomA)
        numerB = random.randrange(1, 65535)
        denomB = random.randrange(2, 65536)
        divisor = src.fractions.Fraction(numerB, denomB)
        exp_numer = numerA * denomB
        exp_denom = denomA * numerB
        expected = src.fractions.Fraction(exp_numer, exp_denom)
        actual = dividend / divisor
        msgPart = str(dividend) + " divided by " + str(divisor)
        message = msgPart + " should be " + str(expected)
        self.assertEqual(expected, actual, message)
    
    def test_reciprocal(self) :
        numer = random.randrange(1, 32767)
        denom = random.randrange(2, 32768)
        instance = src.fractions.Fraction(numer, denom)
        expected = src.fractions.Fraction(denom, numer)
        actual = instance.reciprocal()
        msgPart = "Reciprocal of " + str(instance) + " is " + str(expected)
        message = msgPart + ", got " + str(actual)
        self.assertEqual(expected, actual, message)
    
    def test_is_integer(self) :
        numer = random.randrange(-32768, 32767)
        instance = src.fractions.Fraction(numer, 1)
        message = "Number " + str(instance) + " should be an integer"
        assert instance.is_integer(), message
    
    def test_is_not_integer(self) :
        numer = random.randrange(1, 32767)
        denom = random.randrange(2, 32768)
        instance = src.fractions.Fraction(numer, denom)
        message = "Number " + str(instance) + " should not be an integer"
        assert not instance.is_integer(), message
    
if __name__ == '__main__' :
    unittest.main()
