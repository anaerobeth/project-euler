"""
Circular Primes
Example is 197 where rotations of the digits are themselves prime.
How many circular primes are there below one million?
"""

from collections import deque

def find_rotations(num):
    """ Return a list of digit rotations of the input number """
    rotations = [num]
    digits = list(str(num))
    for k in range(1, len(digits)):
        rotation = int(''.join(digits[k:]+digits[:k]))
        rotations.append(rotation)
    return rotations


def is_prime(num):
    """ Return true if integer input is a prime """
    factors = [1, num]
    # TODO: add factors to list
    return len(factors) == 2


def is_circular_prime(rotations):
    """ Return true if all rotations in the list is prime """
    #TODO: implement
    return rotations.all(lambda x: is_prime(x))


def find_rotations_with_deque(num):
    rotations = []
    d = deque(list(str(num)))
    for _ in enumerate(range(len(d))):
        d.rotate()
        rotations.append(int(''.join(list(d))))

    print(rotations)
    return rotations


assert(find_rotations(197)) == [197, 971, 719]
assert(find_rotations_with_deque(197)) == [719, 971, 197]
assert(is_prime(197)) == True
assert(is_circular_prime(197)) == True



