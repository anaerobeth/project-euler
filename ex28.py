"""
Number spiral diagonals
"""

import itertools

def diagonal_numbers(size):
    diagonal_numbers = [1]
    s = 1
    rounds = size / 2
    # Starting from s, increment by 2 multiplied by round number
    # and append that number to the array
    for i in range(1, rounds+1):
        for _ in itertools.repeat(None, 4):
            # increment the step for every round
            s += i*2
            diagonal_numbers.append(s)
    return diagonal_numbers


if __name__ == '__main__':
    assert sum(diagonal_numbers(5)) == 101

    print(sum(diagonal_numbers(1001))) # 669171001

