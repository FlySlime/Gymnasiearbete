def lehmer(n):
    s = 4
    M = pow(2, n) - 1 # M = 2^n-1
    for _ in range(n - 2): # loops from 1 to n-2
        s = pow(s, 2, M) - 2 # s = s^2 mod M - 2
    if s == 0:
        return True
    else:
        return False
