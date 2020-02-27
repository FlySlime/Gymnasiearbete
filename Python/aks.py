import math


def isPerfectPower(n):
    # If n = a^b for integers a > 1 and b > 1, output composite.
    for b in range(2, round(math.log2(n)) + 1):
        a = pow(n, 1 / b)
        if (a * 10) % 10 == 0:
            return True
    return False


# Temporary
if isPerfectPower(n):
    print("Composite")
