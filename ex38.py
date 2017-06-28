"""
Truncatable primes
"""
def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

for n in range(11, 1000):
    truncatable_primes = []
    target = n
    if is_prime(n):
        while len(str(n)) > 0:
            if is_prime(n):
                return False
            else:
                n = int(str(n)[1:])
        truncatable_primes.append(target)

print(sum((truncatable_primes))

