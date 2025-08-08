import math
import random
import src.numth
import unittest

class TestNumTh(unittest.TestCase) :
    
    SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
                    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
                    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
                    191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
                    257, 263, 269, 271]
    
    NUMBER_OF_SMALL_PRIMES = len(SMALL_PRIMES)
    
    MAXIMUM_TESTING_OMEGA = NUMBER_OF_SMALL_PRIMES // 5
    
    def _choose_squarefree_number(self) :
        omega = random.randrange(1, self.MAXIMUM_TESTING_OMEGA)
        factors = set()
        for i in range(omega - 1) :
            index = random.randrange(0, self.NUMBER_OF_SMALL_PRIMES - 1)
            factor = self.SMALL_PRIMES[index]
            factors.add(factor)
        return math.prod(factors)
    
    def test_squarefree(self) :
        num = self._choose_squarefree_number()
        msg = "Number " + str(num) + " should be found to be squarefree"
        print(msg)
        assert src.numth.squarefree(num), msg
    
    def test_1_is_squarefree(self) :
        assert src.numth.squarefree(1), "1 should be found to be squarefree"

    def test_0_is_not_squarefree(self) :
        assert not src.numth.squarefree(0), "0 shouldn't be found squarefree"

    def test_negative_1_is_squarefree(self) :
        assert src.numth.squarefree(-1), "-1 should be found to be squarefree"

    def test_negative_squarefree(self) :
        num = -self._choose_squarefree_number()
        msg = "Number " + str(num) + " should be found to be squarefree"
        print(msg)
        assert src.numth.squarefree(num), msg
    
    def test_not_squarefree(self) :
        squarefree_kernel = self._choose_squarefree_number()
        index = random.randrange(0, self.NUMBER_OF_SMALL_PRIMES - 1)
        factor = self.SMALL_PRIMES[index]
        square_factor = factor * factor
        num = square_factor * squarefree_kernel
        msg = "Number " + str(num) + " should not be found to be squarefree"
        print(msg)
        assert not src.numth.squarefree(num), msg

    def test_negative_not_squarefree(self) :
        squarefree_kernel = self._choose_squarefree_number()
        index = random.randrange(0, self.NUMBER_OF_SMALL_PRIMES - 1)
        factor = self.SMALL_PRIMES[index]
        square_factor = factor * factor
        num = -square_factor * squarefree_kernel
        msg = "Number " + str(num) + " should not be found to be squarefree"
        print(msg)
        assert not src.numth.squarefree(num), msg

if __name__ == '__main__' :
    unittest.main()
