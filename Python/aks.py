import math


# Step 1
def isPerfectPower(n):
    # If n = a^b for integers a > 1 and b > 1, output composite.
    for b in range(2, round(math.log2(n)) + 1):
        a = pow(n, 1 / b)
        if (a * 10) % 10 == 0:
            return True
    return False


# Step 2
def smallestR(n):
    max_k = math.floor(pow(math.log2(n), 2))
    next_r = True
    r = 2
    while next_r:
        next_r = False
        for k in range(1, max_k):
            if next_r:
                break

            if pow(n, k, r) == 1:
                next_r = 1
            elif pow(n, k, r) == 0:
                next_r = 0
        r += 1
    r -= 1
    return r


# Temporary
n = 31
if isPerfectPower(n):
    print("Composite")
else:
    print(smallestR(n))
