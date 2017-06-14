"""
Lexicographic permutations
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
numbers = []

def permutations(head, tail=''):
    head = map(str, head)
    if len(head) == 0:
        if tail:
            numbers.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])

permutations([0,1,2,3,4,5,6,7,8,9])

print(sorted(map(int, numbers))[999999]) # 2783915460
