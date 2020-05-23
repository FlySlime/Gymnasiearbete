import random


def fermat(n, k):
    if n < 5:  # n under 5 cannot be verified
        return False
    for _ in range(k): # loops from 1 to k
        # random integer between 2 and n-2
        a = random.randint(2, n - 2) 
        # if a^(n-1) is not congruent to 1 (mod n)
        if pow(a, n - 1, n) != 1: 
            return False
        return True
