"""
Integer right triangles
For which value of p ≤ 1000, is the number of solutions maximised?
"""

def right_triangles(perimeter):
    """ Given the perimeter, collect dimensions if they form a right triangle """
    dimensions = []

    # Loop through possible dimensions of the three sides
    for a in range(1, perimeter):
        for b in range(1, perimeter-a):
            c = perimeter - a - b
            # Pythagorean formula for right triangles
            if a*a + b*b == c*c:
                sides = sorted([a, b, c])
                if sides not in dimensions:
                    dimensions.append(sides)
    return dimensions

assert(right_triangles(30)) == [[5, 12, 13]]
assert(right_triangles(120)) == [[20, 48, 52], [24, 45, 51], [30, 40, 50]]


def number_with_max_solutions(limit):
    """ Count possible right triangle dimension combinations for a given perimeter """
    number_with_max_solutions = 0
    max_solutions = 0

    for p in range(3, limit):
        number_of_solutions = len(right_triangles(p))
        if number_of_solutions > max_solutions:
            max_solutions = number_of_solutions
            number_with_max_solutions = p
    return number_with_max_solutions

print(number_with_max_solutions(1000)) # 840
