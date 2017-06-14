"""
Smallest multiple
"""

def is_divisible(num):
    for j in range(10, 20):
        # Exit the loop if early if num % j has a remainder
        if num % j:
            return False
    return True

def smallest_number_divisible():
    i = 20
    while True:
        # Test divisibility of multiples of 20s
        i += 20
        if is_divisible(i):
            return i


if __name__ == "__main__":
    print 'Found {}'.format(smallest_number_divisible()) # 232792560
