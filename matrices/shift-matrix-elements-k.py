# Shift matrix elements row-wise by k https://www.geeksforgeeks.org/shift-matrix-elements-k/

def shiftMatrixByK(matrix, k):
    n = len(matrix)

    if k > n:
        print("Shifting is not possible")
        return 

    j = 0
    while j < n:
        for i in range(k,n):
            print("{}". format(matrix[j][i]), end=" ")

        for i in range(0, k):
            print ("{} " . 
            format(matrix[j][i]), end=" ")
              
        print ("")
        j = j + 1

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
k = 2
  
# Function call
shiftMatrixByK(mat, k)
