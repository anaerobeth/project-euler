"""
10001st prime
"""

def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


n = 1
counter = 0
while counter < 10001:
    if is_prime(n):
        counter += 1
    n += 1

print n - 1


