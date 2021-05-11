# Sort the given matrix https://www.geeksforgeeks.org/sort-given-matrix/

def sortMatrix(matrix):
    n  = len(matrix)
    tempMatrix = []

    for i in range(n):
        for j in range(n):
            tempMatrix.append(matrix[i][j])

    tempMatrix.sort()

    x = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = tempMatrix[x]
            x += 1

def printMatrix(matrix):
    n  = len(matrix)

    for i in range(n):
        print(matrix[i], end="\n")


    print()        

if __name__ == "__main__" :
    matrix = [ 
        [ 5, 4, 7 ],
        [ 1, 3, 8 ],
        [ 2, 9, 6 ] ]
    print( "Original Matrix:")
    printMatrix(matrix)

    sortMatrix(matrix)
    print("\nMatrix After Sorting:")
    printMatrix(matrix)

