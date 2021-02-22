# Connected Cells in a Grid https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

def connectedCell(matrix):
    maxCellCounter = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                regionCellCount = countRegionCell(matrix, row, col)
                maxCellCounter = max(maxCellCounter, regionCellCount)
    
    return maxCellCounter            

def countRegionCell(matrix, row, col):
    if any([row < 0, col < 0, row >= len(matrix), col >= len(matrix[0])]):
        return 0

    if matrix[row][col] == 0:
        return 0

    cellCount = 1
    matrix[row][col] = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col +2):
            if any([ r != row, c != col]):
                cellCount += countRegionCell(matrix, r, c)

    return cellCount


print connectedCell([
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
])                