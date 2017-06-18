"""
Digit factorials
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""

from itertools import accumulate

def sum_factorials(num):
    result = [ factorial(int(i)) for i in str(num) ]
    return sum(result)


def factorial(digit):
    product = 1
    for i in range(1, digit+1):
        product *= i
    return product


assert factorial(4) == 24
assert sum_factorials(145) == 145

# Estimate range of numbers to test
# print sum_factorials(99) # 725760
# print sum_factorials(55) # 240
# print sum_factorials(1111) # 4
# Note: Since even large numbers can have small sum_factorials,
# can we set a stopping point at which we are confident we cant find more?


def find_matches(ceiling):
    """ Collect numbers matching sum the of their factorials """
    result = [ i for i in range(3, ceiling) if i == sum_factorials(i) ]

    return list(accumulate(result))


# assert find_matches(10000) == [145]
# assert find_matches(100000) ==  [145, 40585]

# assert sum(find_matches(10000)) == 145
# assert sum(find_matches(100000)) ==  40730
# assert sum(find_matches(1000000)) ==  40730
# assert sum(find_matches(10000000)) ==  40730

print(sum(find_matches(100000))) # 40730

