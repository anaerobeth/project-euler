"""
Longest Collatz sequence
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?
"""
def sequence(num):
    chain = [num]

    while num != 1:
        if (num % 2 == 0):
            num = num // 2
        else:
            num =  (3 * num) + 1
        chain.append(num)

    return chain


def brute_force_solution():
    longest_chain_length = 1
    king = 1

    for num in range(1, 1000000):
        length = len(sequence(num))
        if length > longest_chain_length:
            longest_chain_length = length
            king = num

    return king # 837799
