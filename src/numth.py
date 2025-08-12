import math

# TODO: Optimize, fine-tune
def squarefree(num) :
    """Determines if a number is squarefree or not.
    
    Args:
        num: The number to determine whether it is squarefree or not. For 
        example, 46, 47 and 48. May be 0 or negative.
    Returns:
        True if the number is divisible by no perfect square other than 1, 
        otherwise false. In the example, this function returns true for 46 and 
        47, as the former is twice 23 and the latter is a prime number; but it 
        returns false for 48 as that is thrice 16, the square of 4.
    """
    if num % 4 == 0 :
        return False
    threshold = math.sqrt(abs(num))
    all_distinct_so_far = True
    root = 3
    while all_distinct_so_far and root <= threshold :
        square = root * root
        all_distinct_so_far = (num % square != 0)
        root += 2
    return all_distinct_so_far
