import random


def fermat(n, k):
    # Use _ as "index" variable - means no declared variable
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
        return True
