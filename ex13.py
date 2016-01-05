"""
Large sum
first ten digits of the sum
"""


with open('ex13_input.txt', 'r') as f:
    total = 0
    for line in f:
        total += int(line.rstrip())
    print str(total)[:10]
