import math


# Step 1
def isPerfectPower(n):
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
                next_r = True
            elif pow(n, k, r) == 0:
                next_r = False
        r += 1
        if math.gcd(r - 1, n) != 1:
            next_r = True
    r -= 1
    return r


# Step 3
def checkDivisors(n, r):
    for a in range(r, 1, -1):
        if math.gcd(a, n) > 1 and math.gcd(a, n) < n:
            return True
        return False


# Step 4
def boolCheck(n, r):
    if n <= r:
        return True
    return False


# Step 5
def totient(k):
    totatives = []
    for a in range(1, k + 1):
        if math.gcd(k, a) == 1:
            totatives.append(a)
    return len(totatives)


# def step5(n, r):
#     for a in range(1, math.floor(math.sqrt(totient(r))*math.log(n, 2))):
#         # this needs to be finished


def AKS(n):
    if n % 2 == 0:
        return "Composite"

    if isPerfectPower(n):
        return "Composite"

    r = smallestR(n)

    if checkDivisors(n, r):
        return "Composite"

    if n <= 5690034:
        if boolCheck(n, r):
            return "Prime"
    # add step 5 here
    return "owo"


print(AKS(int(input())))
