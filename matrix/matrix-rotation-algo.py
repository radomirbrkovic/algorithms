# Matrix Layer Rotation https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

def matrixRotation(matrix, r):
    mat = []
    k = min(n, m) // 2

    for i in range(k):
        tmp = []
        for j in range(i, n-1-i):
            tmp.append(matrix[i][j])
        for j in range(i, m - 1 -i):
            tmp.append(matrix[i][n-1-i])
        for j in range(n - 1 -i, i, -1):
            tmp.append(matrix[m-1-i][j])   
        for j in range(m-1-i, i, -1):
            tmp.append(matrix[i][j])       

        mat.append(tmp) 

    # rottating elements
    for i in range(k):
        row= mat[i]
        idx = r % len(row)

        def inc():
            return  (idx+1) % len(row)

        for j in range(i, n-1-i):
            matrix[i][j] = row[idx]
            idx = inc()
        for j in range(i, m - 1 -i):
            matrix[i][n-1-i] =row[idx]
            idx = inc()
        for j in range(n - 1 -i, i, -1):
            matrix[m-1-i][j] = row[idx]
            idx = inc() 
        for j in range(m-1-i, i, -1):
            matrix[i][j] = row[idx]
            idx = inc()       

    for row in matrix:
        print(*row)

matrixRotation([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
], 2)     