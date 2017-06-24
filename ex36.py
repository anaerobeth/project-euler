"""
Double-base palindromes
Find the sum of all numbers under 1M which are palindromic in base 10 and base 2
"""

def is_palindrome(num):
    num = str(num)
    if len(num) == 1: return True
    if len(num) == 2 and num[0] == num[1]: return True
    if num[0] != num[-1]:
        return False
    else:
        return is_palindrome(num[1:-1])


def binary(num):
    # int("{0:b}".format(num))
    return int(format(num, 'b'))


def binary_recursive(num):
    if num < 0: return 'Invalid input'
    if num == 0: return ''
    else:
        return binary_recursive(num // 2) + str(num % 2)

def binary_loop(num):
    value = ''
    while num != 0:
        value = str(num % 2) + value
        num //= 2
    return int(value)

def double_base_palindromes(max):
    return [i for i in range(1, max) if is_palindrome(i) and is_palindrome(binary(i))]


assert(is_palindrome(121)) == True
assert(is_palindrome(1221)) == True
assert(is_palindrome(123)) == False

assert(binary(2)) == 10
assert(binary(4)) == 100
assert(binary(585)) == 1001001001
assert(binary_loop(585)) == 1001001001
assert(int(binary_recursive(585))) == 1001001001

assert(double_base_palindromes(1000)) == [1, 3, 5, 7, 9, 33, 99, 313, 585, 717]

print(sum(double_base_palindromes(10000000))) # 25846868
