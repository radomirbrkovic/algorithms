# Swap major and minor diagonals of a square matrix https://www.geeksforgeeks.org/swap-major-minor-diagonals-square-matrix/

def swapDiagonal(matrix):
    N = len(matrix) 
    for i in range(N):
         
        matrix[i][i], matrix[i][N-i-1] = \
            matrix[i][N-i-1], matrix[i][i]

matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]
 
# swap diagonals of matrix
swapDiagonal(matrix)
 
for i in range(len(matrix)):   
    for j in range(len(matrix)):       
        print(matrix[i][j], end = ' ')       
    print()            