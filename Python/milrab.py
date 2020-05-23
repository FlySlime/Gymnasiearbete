import random


def findIntegers(n):
    counter = 0
    number = n - 1
    # the loop counts the times 'number' can be divded by 2
    while number % 2 == 0:
        counter += 1
        number //= 2
    # remaining 'number' and the counter is returned
    return (counter, number)


def millerRabin(n, k):
    if n < 5:  # n under 5 cannot be verified
        return False

    # calls on a function that
    # returns the value for r and d
    r, d = findIntegers(n)
    for _ in range(k): # loops k times, k = rounds
        # random integer between 2 and n-2
        a = random.randint(2, n - 2)
        # x = x^d mod (n)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            # x = x^2 mod (n)
            x = pow(x, 2, n)
            if x == 1:
                return False
        if x == n - 1:
            continue
        return False
    return True
