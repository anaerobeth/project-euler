"""
Special Pythagorean triplet
"""

def is_triplet(a, b, c):
    return a * a + b * b == c * c

assert is_triplet(3, 4, 5)

for a in range(1, 333):
    for b in range(a, 667):
        c = 1000 - a - b
        if is_triplet(a, b, c):
            print "{} + {} + {} = 1000".format(a, b, c)
            print "Product is {}".format(a * b * c)
            break
    else:
        continue
    break
