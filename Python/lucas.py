def lehmer(n):
    s = 4
    M = pow(2, n) - 1
    for i in range(n - 2):
        s = pow(s, 2, M) - 2
    if s == 0:
        return True
    else:
        return False
