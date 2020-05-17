import random


def fermat(n, k):
    if n < 5:  # n under 5 cannot be verified
        return False
    for _ in range(k): # loops from 1 to k
        a = random.randint(2, n - 2) # a = random integer between 2 and n-2
        if pow(a, n - 1, n) != 1: # if a^(n-1) is not congruent to 1 mod n
            return False
        return True
