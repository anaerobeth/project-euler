"""
Sum of powers
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_powers(digit, power):
    """ Raise each digit to specified power then get their total"""
    running_total = 0
    for i in str(digit):
        running_total += int(i)**power

    return running_total

# Estimate the range of numbers to test
# print sum_of_powers(  9999, 5) # 236196 - good
# print sum_of_powers( 99999, 5) # 295245 - good
# print sum_of_powers(999999, 5) # 354294 - sum is lower than number
# print sum_of_powers(299999, 5) # 295277 - sum is lower than number
# print sum_of_powers(199999, 5) # 295488 - good


def find_numbers(power):
    """ Collect numbers that are equal to the sum of their powers"""
    numbers_equal_to_sum_of_powers = []
    for n in range(2, 299999):
        if sum_of_powers(n, power) == n:
            numbers_equal_to_sum_of_powers.append(n)

    return numbers_equal_to_sum_of_powers


if __name__ == '__main__':
    assert sum_of_powers(1634, 4) == 1634
    assert sum_of_powers(9474, 4) == 9474

    assert find_numbers(4) == [1634, 8208, 9474]

    print sum(find_numbers(5)) # 443839
