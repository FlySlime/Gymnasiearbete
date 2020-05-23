import math


def smartBrute(n):
    if n % 2 == 0: # if n is an even number
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    # loops from 3 to sqrt(n), increases with 2 every loop
    for x in range(3, math.isqrt(n) + 1, 2):
        if n % x == 0:
            return False
    return True
