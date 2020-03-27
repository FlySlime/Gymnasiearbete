import math


def smartBrute(n):
    if n % 2 == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(3, math.isqrt(n) + 1, 2):
        if n % x == 0:
            return False
    return True
