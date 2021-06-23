# Print matrix in antispiral form https://www.geeksforgeeks.org/print-matrix-antispiral-form/

def antiSpiralTraversal(matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    k = 0
    l = 0

    stk = []

    while (k < cols and l < rows):
        for i in range(l, rows):
            stk.append(matrix[k][i])

        k += 1

        for i in range(k, cols):
            stk.append(matrix[i][rows - 1])

        rows -= 1

        if (k < cols):
            for i in range(rows-1, l - 1, -1):
                stk.append(matrix[cols-1][i])
            cols -= 1

        if(l < rows):
            for i in range(cols-1, k - 1, -1):
                stk.append(matrix[i][l])

            l += 1                            

    while len(stk) > 0:
        print(str(stk[-1]), end = " ")
        stk.pop()

mat = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]        
        
antiSpiralTraversal(mat)        