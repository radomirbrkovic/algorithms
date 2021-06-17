# Sort the matrix row-wise and column-wise https://www.geeksforgeeks.org/sort-matrix-row-wise-column-wise/

MAX_SIZE = 10

def sortByRow(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i].sort()


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i +1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def sortMatRowAndColWise(matrix):
    sortByRow(matrix)
    transpose(matrix)
    sortByRow(matrix)
    transpose(matrix)

def printMat(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j] ), end = " ")
        print();

matrix = [
        [ 4, 1, 3 ],
        [ 9, 6, 8 ],
        [ 5, 2, 7 ]
    ]

print("Original Matrix:")
printMat(matrix)
 
sortMatRowAndColWise(matrix)
 
print("\nMatrix After Sorting:")
printMat(matrix)

