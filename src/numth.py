import math

# TODO: Optimize, fine-tune
def squarefree(num) :
    if num == 1 :
        return True
    if num == 0 :
        return False
    if num == -1 :
        return True
    if num < -1 :
        return True
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
