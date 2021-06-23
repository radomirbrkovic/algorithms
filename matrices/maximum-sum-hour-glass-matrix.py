# Maximum sum of hour glass in matrix https://www.geeksforgeeks.org/maximum-sum-hour-glass-matrix/

def maxSum(matrix):
    maxSum = -50000
    R = len(matrix[0])
    C = len(matrix)

    if R < 3 or C < 3:
        return -1

    for i in range(R-2):
        for j in range(C-2):
            SUM = (matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]) + (matrix[i + 1][j + 1]) + (matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2])    

            if SUM > maxSum:
                maxSum = SUM
            else:
                continue

    return maxSum



matrix = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]
res = maxSum(matrix)
 
if(res == -1):
    print("Not possible")
else:
    print(f"Maximum sum of hour glass = {res}")