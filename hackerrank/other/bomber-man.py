# The Bomberman Game https://www.hackerrank.com/challenges/bomber-man/problem

def bomberMan(n, grid):
    if n == 1:
       return grid

    if n % 2 == 0:
        return ['O' * c for i in range(r)]

    n //=2

    for q in range((n+1) % 2 + 1):
        newGrid = [['O'] * c for i in range(r)]

        def set(x, y):
            if 0 <= x < r and 0 <= y < c:
                newGrid[x][y] = '.'

        xi = [0, 0, 0, 1, -1]
        yi = [0, -1, 1, 0, 0]    

        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':

                    for i, j in zip(xi, yi):
                        set(x + i, y + j)

        grid = newGrid


    return ["". join(x) for x in grid]                    



