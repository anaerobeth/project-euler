"""
Number spiral diagonals
"""

import itertools

def sum_of_diagonal_numbers(size):
    s = 1
    running_total = 1
    rounds = size / 2
    # Starting from s, increment by 2 multiplied by round number
    # and update the running total
    for i in range(1, rounds+1):
        for _ in itertools.repeat(None, 4):
            # increment the step for every round
            s += i*2
            running_total += s
    return running_total


if __name__ == '__main__':
    assert sum_of_diagonal_numbers(5) == 101

    print(sum_of_diagonal_numbers(1001)) # 669171001

