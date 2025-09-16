import random
import unittest

from src.algnums import AlgebraicInteger
from src.rings import IntegerRing

class AlgebraicIntegerTest(unittest.TestCase) :
    
    def test_str_negative(self) :
        n = random.randrange(1, 32767)
        instance = AlgebraicInteger(-n)
        expected = f"\u2212{n}"
        actual = str(instance)
        self.assertEqual(expected, actual)
    
    def test_str_zero(self) :
        instance = AlgebraicInteger(0)
        expected = "0"
        actual = str(instance)
        self.assertEqual(expected, actual)
        
    def test_str_positive(self) :
        n = random.randrange(1, 32767)
        instance = AlgebraicInteger(n)
        expected = str(n)
        actual = str(instance)
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
        expected = f"&minus;{n}"
        actual = instance.HTML_str()
        self.assertEqual(expected, actual)
        
    def test_TeX_str(self) :
        n = random.randrange(-32768, 32767)
        instance = AlgebraicInteger(n)
        expected = str(n)
        actual = instance.TeX_str()
        self.assertEqual(expected, actual)
    
    def test_eq(self) :
        n = random.randrange(-32768, 32767)
        some_integer = AlgebraicInteger(n)
        same_integer = AlgebraicInteger(n)
        num_str = str(n)
        message = num_str + " should equal " + num_str
        self.assertEqual(some_integer, same_integer, message)
    
    def test_not_equal(self) :
        nA = random.randrange(-32768, 32767)
        nB = nA + random.randrange(1, 32768) + 1
        some_integer = AlgebraicInteger(nA)
        other_integer = AlgebraicInteger(nB)
        message = f"{nA} should not equal {nB}"
        self.assertNotEqual(some_integer, other_integer, message)
        
    def test_ring(self) :
        n = random.randrange(-32768, 32767)
        instance = AlgebraicInteger(n)
        expected = IntegerRing()
        actual = instance.ring()
        self.assertEqual(expected, actual)
        
    def test_algebraic_degree(self) :
        n = 0
        while n == 0 :
            n = random.randrange(-65536, 65535)
        instance = AlgebraicInteger(n)
        expected = 1
        actual = instance.algebraic_degree()
        self.assertEqual(expected, actual)
        
    def test_algebraic_degree_of_zero(self) :
        expected = 0
        instance = AlgebraicInteger(expected)
        actual = instance.algebraic_degree()
        self.assertEqual(expected, actual)
    
    def test_trace(self) :
        expected = random.randrange(-65536, 65535)
        instance = AlgebraicInteger(expected)
        actual = instance.trace()
        self.assertEqual(expected, actual)
        
    def test_norm(self) :
        expected = random.randrange(-65536, 65535)
        instance = AlgebraicInteger(expected)
        actual = instance.norm()
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
    
    def test_add(self) :
        nA = random.randrange(-65536, 65535)
        nB = random.randrange(-65536, 65535)
        addendA = AlgebraicInteger(nA)
        addendB = AlgebraicInteger(nB)
        addition = nA + nB
        expected = AlgebraicInteger(addition)
        actual = addendA + addendB
        message = f"Adding up {nA} and {nB}, expected {addition}, got {actual}"
        self.assertEqual(expected, actual, message)

    def test_sub(self) :
        nA = random.randrange(-65536, 65535)
        nB = random.randrange(-65536, 65535)
        minuend = AlgebraicInteger(nA)
        subtrahend = AlgebraicInteger(nB)
        subtraction = nA - nB
        expected = AlgebraicInteger(subtraction)
        actual = minuend - subtrahend
        message = f"Subtract {nB} from {nA} expected {subtraction} got {actual}"
        self.assertEqual(expected, actual, message)
    
    def test_neg(self) :
        n = random.randrange(1, 1048576)
        negatedN = -n
        instance = AlgebraicInteger(n)
        expected = AlgebraicInteger(negatedN)
        actual = -instance
        message = f"{n} negated should be {negatedN}, got {actual}"
        self.assertEqual(expected, actual, message)

    def test_negate_negative(self) :
        n = -random.randrange(1, 1048576)
        negatedN = -n
        instance = AlgebraicInteger(n)
        expected = AlgebraicInteger(negatedN)
        actual = -instance
        message = f"{n} negated should be {negatedN}, got {actual}"
        self.assertEqual(expected, actual, message)
    
    def test_negate_zero(self) :
        expected = AlgebraicInteger(0)
        actual = -expected
        message = f"Expected 0, got {actual}"
        self.assertEqual(expected, actual, message)
    
    def test_mul(self) :
        nA = random.randrange(-128, 127)
        nB = random.randrange(-128, 127)
        multiplicandA = AlgebraicInteger(nA)
        multiplicandB = AlgebraicInteger(nB)
        product = nA * nB
        expected = AlgebraicInteger(product)
        actual = multiplicandA * multiplicandB
        message = f"{nA} times {nB} should be {product}, got {actual}"
        self.assertEqual(expected, actual, message)
    
    def test_floordiv_exact_negative(self) :
        exp_n = random.randrange(-128, -1)
        divisor_n = random.randrange(2, 128)
        dividend_n = exp_n * divisor_n
        dividend = AlgebraicInteger(dividend_n)
        divisor = AlgebraicInteger(divisor_n)
        expected = AlgebraicInteger(exp_n)
        actual = dividend // divisor
        message = f"{dividend_n} div {divisor_n}, exp. {exp_n}, got {actual}"
        self.assertEqual(expected, actual, message)

    def test_floordiv_exact_positive(self) :
        exp_n = random.randrange(1, 127)
        divisor_n = random.randrange(2, 128)
        dividend_n = exp_n * divisor_n
        dividend = AlgebraicInteger(dividend_n)
        divisor = AlgebraicInteger(divisor_n)
        expected = AlgebraicInteger(exp_n)
        actual = dividend // divisor
        message = f"{dividend_n} div {divisor_n}, exp. {exp_n}, got {actual}"
        self.assertEqual(expected, actual, message)

    # TODO: Tests for __truediv__(), more tests for __floordiv__()
    
    # TODO: Tests for division by zero
        
if __name__ == '__main__' :
    unittest.main()
