import math


def isPerfectPower(n):
    # Generate all divisors up to log2(n)
    divisors = []
    for x in range(2, math.ceil(math.log2(n)) + 1):
        if n % x == 0:
            divisors.append(x)

    if len(divisors) == 0:
        return False

    i = 2
    while pow(divisors[0], i) <= n:
        for div in divisors:
            if pow(div, i) == n:
                return True
        i += 1
    return False


# Temporary
n = 36
if isPerfectPower(n):
    print("Composite")
