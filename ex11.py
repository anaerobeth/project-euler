"""
Largest product in a grid
"""

def products(i, j, grid, max_prod):
    cprod, rprod, rdprod, ldprod = 0, 0, 0, 0
    if i < 16: 
        cprod = grid[i][j] * grid[i+1][j]  * grid[i+2][j] * grid[i+3][j]
    if j < 16:
        rprod = grid[i][j] * grid[i][j+1]  * grid[i][j+2] * grid[i][j+3]
    if i < 16 and j < 16: 
        rdprod = grid[i][j] * grid[i+1][j+1]  * grid[i+2][j+2] * grid[i+3][j+3]
    if j > 4 and i < 16: 
        ldprod = grid[i][j] * grid[i+1][j-1]  * grid[i+2][j-2] * grid[i+3][j-3]

    print "{}, {}, {}, {}".format(rprod, cprod, rdprod, ldprod)
    local_max = max([rprod, cprod, rdprod, ldprod])
    if max_prod < local_max:
        max_prod = local_max
    return max_prod


with open('ex11_input.txt' , 'r') as f:
    grid = []
    for line in f:
        grid.append(map(int, line.rstrip().split(' ')))

    assert len(grid) == 20


print grid[0]
print grid[0][1]

max_prod = 0
for i in range(20):
    for j in range(20):
        max_prod = products(i, j, grid, max_prod)

print max_prod
