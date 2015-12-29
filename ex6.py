"""
Sum square difference
"""

def sum_of_squares(num):
    return sum(x*x for x in range(101))

def square_of_sum(num):
    total = sum(x for x in range(101))
    return total * total


print square_of_sum(10) - sum_of_squares(10)
