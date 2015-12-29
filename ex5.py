"""
Smallest multiple
"""

def evenly_divisible(num):
    for j in range(10, 20)  :
       if num % j:
           return False
    return True

i = 20
while True:
    i += 20
    if evenly_divisible(i):
        print 'Found {}'.format(i)
        break

