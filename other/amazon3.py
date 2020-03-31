def numberAmazonGoStores(rows, column, grid):
    result = 0
    for i in range(rows):
        rowCounter = 0

        for j in range(column):
            if j < column-1:
                if grid[i][j] == 1 and grid[i][j+1] == 1:
                    rowCounter =1 
                    break;
                elif i < rows - 1:
                    if grid[i][j] == 1 and grid[i+1][j] == 1:
                        rowCounter =1 
                        break; 
                    elif grid[i][j] == 1 and grid[i+1][j+1] == 1:
                        rowCounter = 1
                        break       
            else:
                if i == rows - 1:
                    if grid[i][j] == 1 and grid[i-1][j] == 1:
                        rowCounter =1 
                        break; 
                    elif grid[i][j] == 1 and grid[i-1][j-1] == 1:
                        rowCounter = 1
                        break     
                  
        result += rowCounter


    return result


matrix = [
    [1,1,0,0],
    [0,0,0,0],
    [0,0,1,1],
    [0,0,0,0]
]

matrix2 = [
    [1,1,0,0],
    [0,0,1,0],
    [0,0,0,0],
    [1,0,1,1],
    [1,1,1,1]
]


matrix3 = [
  [1, 0, 0, 0, 0, 0, 0],  
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1],  
]

print numberAmazonGoStores(7, 7, matrix3)