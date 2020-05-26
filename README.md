# Prime Numbers - Gymnasiearbete

Prime numbers are a fundamental part of number theory. Primes have many special
properties that can be exploited. One of the most common applications being
RSA-encryption, which uses a product of two large primes as a key. The rise of
more powerful computers has led to weaker keys being cracked. Therefore it is in
a computer scientist's interest to find larger primes. In order to accomplish
this, efficient algorithms have to be developed. This study investigates the
efficiency of five simple primality testing algorithms:

- Brute-force
- Smart Brute-force
- Lucas-Lehmer
- Miller-Rabin
- Fermat Primality Test

In the first test, the algorithms were given the task of finding the largest
prime number within 60 seconds. The test was performed by looping through the
natural numbers starting from 2. The first test could not include
Lucas-Lehmer, as it only works for mersenne numbers. In the first test it was
determined that the Fermat primality test found the largest prime.

In the second test, the algorithms were given mersenne primes of different sizes
and returned the time it took for them to finish verifying that it was a prime.
However, if the time exceeded 120 seconds, the test case would be deemed as a
"failure" and immediately end the program. These tests concluded that
Lucas-Lehmer was the fastest algorithm to verify mersenne primes. 

The purpose of this study is not to find newer primes, but rather to demonstrate
the correlation between the Big O notation and run-times, as-well as giving an
introduction to primality testing algorithms. 

## Built With

-   [LaTeX](https://www.latex-project.org/) - The typesetting system for the entire essay
-   [Python](https://www.python.org/) - The programming language to perform the tests

## Authors

-   **Ibrahim Abdulhussein** - [flyslime](https://github.com/flyslime)
-   **Robin Brusbo** - [robinbrusbo](https://github.com/robinbrusbo)

## Acknowledgements

-   Belal Tulimat 
-   Bertil Nilsson
-   Björn Norén
-   Jonas Ingesson
