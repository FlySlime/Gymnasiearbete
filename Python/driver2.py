# This driver file tests if an algorithm can solve
# a mersenne prime within two minutes. If it cannot,
# the driver code will print the mersenne prime it failed
# on with an 'X'. However, if it succeeded, it will
# instead print an 'O' and the time it took.
#
# Change line 58 to desired algorithm, i.e. brute(n).
#
# Make sure fermat and millerRabin are written as
# <function>(n, 10). Where 10 is k, the second parameter

import time

# from FILE import FUNCTION
from brute import brute
from smartbrute import smartBrute
from lucas import lehmer
from fermat import fermat
from milrab import millerRabin


def driver():
    # 13 exponents for mersenne primes
    # Taken from https://en.wikipedia.org/wiki/Mersenne_prime
    exponent = [
        19,
        31,
        61,
        107,
        607,
        1279,
        4423,
        9689,
        11213,
        19937,
        23209,
        44497,
        86243,
    ]
    for n in exponent:
        start = time.time()
        timelimit = time.time() + 120  # 120 seconds
        primeTest(pow(2, n) - 1)
        if timelimit > time.time():
            print(
                  str(n) + ": O\nTime: " +
                  str(time.time() - start) + " seconds\n"
                 )
        else:
            print(
                  str(n) + ": X\nTime: " +
                  str(time.time() - start) + " seconds\n"
                 )
            return


def primeTest(n):
    if smartBrute(n):  # Algorithm change here
        return True
    return False


if __name__ == "__main__":
    driver()
