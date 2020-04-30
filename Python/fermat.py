import random


def fermat(n, k):
    if n < 5:  # n under 5 cannot be verified
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
        return True
