"""
Power digit sum
What is the sum of the digits of the number 2^1000?
"""

num = 1
for i in range(1000):
    num *= 2

num_list = map(int, (str(num)))
print sum(num_list)
