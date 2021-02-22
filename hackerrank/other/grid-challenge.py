# Grid Challenge https://www.hackerrank.com/challenges/grid-challenge/problem


def gridChallenge(grid):

    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < grid[i-1][j]:
                return 'NO'

    return 'YES'             

print gridChallenge(['abc', 'ade', 'efg'])    
print gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])    