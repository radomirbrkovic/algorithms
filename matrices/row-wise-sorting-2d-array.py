# Row wise sorting in 2D array https://www.geeksforgeeks.org/row-wise-sorting-2d-array/

def sortRowWise(matrix):
    
    for i in range(len(matrix)):
        matrix[i].sort()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

sortRowWise([
    [9, 8, 7, 1 ],
    [7, 3, 0, 2],
    [9, 5, 3, 2],
    [ 6, 3, 1, 2 ]
    ])        