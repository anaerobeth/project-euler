"""
Longest Collatz sequence
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?
"""
def next_number(num):
    if (num % 2 == 0):
        return num / 2
    else:
        return (3 * num) + 1

for num in range(100):
    chain = []
    while num != 1:
        child = next_number(num)
        num = child
