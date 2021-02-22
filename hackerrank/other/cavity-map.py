#Cavity Map https://www.hackerrank.com/challenges/cavity-map/problem


def cavityMap(grid):
    grid = [list(x) for x in grid]

    for i in range(1, n-1):
        for j in range (1, n -1):
            if grid[i][j] > grid[i - 1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j - 1] and grid[i][j] > grid[i][j + 1]:
                grid[i][j] = "X"

    return ["". join(x) for x in grid]



print cavityMap(['989', '919', '111'])
print cavityMap(['1112', '1912', '1892', '1234'])