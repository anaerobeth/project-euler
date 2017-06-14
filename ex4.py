"""
Largest palindrome product
"""

def max_palindrome(i, j, m):
    product = i * j
    if str(product) == str(product)[::-1]:
        if product > m:
            m = product
    return m

if __name__ == "__main__":
    digits = range(101, 999)
    largest_palindrome = 0

    for i in digits:
        for j in digits:
            largest_palindrome = max_palindrome(i, j, largest_palindrome)

    print largest_palindrome


