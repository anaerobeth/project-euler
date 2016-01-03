"""
Highly divisible triangular number
Ref: http://www.mathblog.dk/triangle-number-with-more-than-500-divisors/
"""
counter = 0
triangle = 0
divisors = 0

while divisors < 501:
    counter += 1
    triangle += counter
    divisors = 0
    int_sqrt_triangle = int(triangle**(1.0/2))

    for i in range(1,int_sqrt_triangle):
        if triangle % i == 0:
            divisors += 2
    # if number is perfect square, remove extra divisor
    if int_sqrt_triangle * int_sqrt_triangle ==  triangle:
        divisors -= 1


print "{} has {} divisors".format(triangle, divisors)
