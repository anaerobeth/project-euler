"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = 1000

# Solution using a loop
sum = 0
for i in range(1, n):
   if i % 3 == 0 or i % 5 == 0:
       sum += i
print sum


# Solution using summation of parts
def k(n, i):
    # 3 * 999/3 * (999/3)+1 / 2
    # 5 * 999/5 * (999/5)+1 / 2
    # 15 * 999/15 * (999/15)+1 / 2
    return i * int((n-1)/i) * ((n-1)/i + 1) / 2

multiples_of_3 = k(n, 3)
multiples_of_5 = k(n, 5)
multiples_of_15 = k(n, 15)

# remove double-counted multiples of 15
sum = multiples_of_3 + multiples_of_5  - multiples_of_15
print sum

