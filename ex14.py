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


def fast_sequence(n, d):
    print('Entering: ', d)
    if d[n] != None: return d[n]
    print('Dict is: ', d)
    if n % 2 == 0:
        print('Even: ', d)
        d[n] = fast_sequence(n/2, d)
    else:
        print('Odd: ', d)
        d[n] = fast_sequence(3*n+1, d)
    return d


def build_sequence_dict(limit):
    d = { 1: 1 }

    for n in range(1, limit):
        print('Building sequence: ', n)
        fast_sequence(n, d)


def dict_solution(limit):
    print('In dict solution')
    build_sequence_dict(limit)
    return max(d, key=lambda key: d[key]) # 837799


def main():
    print(dict_solution(100))

if __name__ == '__main__':
    main()
