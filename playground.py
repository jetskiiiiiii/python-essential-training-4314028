from math import *

"""
finding primes up until num
- get sqrt of num
- find primes up until sqrt
- find if those primes are divisors of num
- if no divisors, 

For each number, in order to determine if it is prime, take the following steps:
1. Find the square root of the number
2. Find all the primes up to that square root
3. Test to see if any of those primes are divisors 

If a number has no prime divisors, it is prime!

- 0-100
- every number in range, get its sqrt
- find primes up to that sqrt
- find if primes are divisors of number
- if no prime divisors, number is prime
"""

num = 88
primes_inside = []


def isPrime(num):
    square = int(num**0.5) + 1
    for i in range(2, square):  # 2-10
        # find if i is prime
        for j in range(2, int(i / 2) + 1):  # 2,3,5,7
            if i % j == 0:
                break  # (2,2,break) ()
        if num % i == 0:
            print("Not a prime")
            return False
    return True


print(isPrime(num))
