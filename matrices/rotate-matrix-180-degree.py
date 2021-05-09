# Rotate a Matrix by 180 degree https://www.geeksforgeeks.org/rotate-matrix-180-degree/


def rotateMatrix(matrix):
    N = len(matrix)
    i = N - 1

    while i >= 0:
        j = N - 1
        while j >= 0:
            print(matrix[i][j], end=" ")
            j = j - 1
        print()
        i = i - 1


# Driven code
mat = [[1, 2, 3],
       [ 4, 5, 6 ],
       [ 7, 8, 9 ]]
rotateMatrix(mat)