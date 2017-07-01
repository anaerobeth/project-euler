"""
Pandigital prime
An n-digit number is pandigital if it uses digits 1 to n exactly once.
What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations

def pandigitals(n):
    """ Build a sorted set of numbers that use each digit once """

    digits = permutations(range(1,n+1))

    return list(reversed(sorted(digits)))

assert(pandigitals(3)) == [(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False

    # Loop up to the square root of n, step 2 to skip evens
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True

assert(is_prime(12)) == False
assert(is_prime(13)) == True
assert(is_prime(145)) == False
assert(is_prime(54321)) == False


def largest_pandigital_prime(n):
    """ Given the number of digits, go through all possible permutations
    starting from largest and stop when a prime number is identified """

    largest = 0

    for n in range(2, n+1):
        for digits in pandigitals(n):
            target = int(''.join(str(d) for d in digits))

            if is_prime(target) == True:
                if target > largest:
                    largest = target
    return largest


print(largest_pandigital_prime(9))  # 7652413
