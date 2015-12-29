"""
Largest palindrome product
"""

def max_palindrome(i, j, x):
    product = i * j
    if str(product) == str(product)[::-1]:
        if product > m:
            m = product
    return m

digits = range(101, 999)
m = 0

for i in digits:
    for j in digits:
        m = max_palindrome(i, j, m)

print m


