"""
Largest palindrome product
"""

def max_palindrome(i, j, max):
    product = i * j
    if str(product) == str(product)[::-1]:
        if product > max:
            max = product
    return max

digits = range(101, 999)
max = 0

for i in digits:
    for j in digits:
        max = max_palindrome(i, j, max)

print max


