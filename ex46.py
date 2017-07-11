"""
Goldbach's other conjecture
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

def smaller_primes(num):
    """ list of primes less than the number """
    primes = []
    for n in range(1, num//2, 2):
        primes.append(n)

    return primes


def goldbach_exception(num):
    """ cannot be written as the sum of a prime and twice a square """
    result = None
    for prime in smaller_primes(num):
        print("Prime: ", prime)
        keep_going = True
        counter = 1

        while keep_going:
            """ compare num with goldbach_sum until match but exit when exceeded """ 
            goldbach_sum = prime + 2*counter*counter
            print("  Sum: ", goldbach_sum)
            if num == goldbach_sum:
                result = 'foo'
                keep_going = False
            elif num > goldbach_sum:
                print('     looping')
                counter += 1
            else:
                keep_going = False
                result = num

    print("********** ", result)
    return result


def odd_composites(limit):
    """ loop through composite odds and check if goldbach_conformant """
    pass

# assert(smaller_primes(16)) == [1, 3, 5, 7]
# assert(goldbach_exception(9)) == 9
# assert(goldbach_exception(33)) == 33
print(goldbach_exception(9))
