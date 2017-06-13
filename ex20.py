def factorial(num):
    temp = 1
    for i in range(1, num):
        temp *= i
    return temp


def sum_of_factorial_digits(num):
    # this also works
    # sum(int(n) for n in str(temp))
    temp = factorial(num)
    return sum(map(int, str(temp)))

assert sum_of_factorial_digits(10) == 27
print(sum_of_factorial_digits(100))
