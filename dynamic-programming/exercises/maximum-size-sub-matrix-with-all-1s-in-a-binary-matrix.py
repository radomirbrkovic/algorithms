# Maximum size square sub-matrix with all 1s https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

def printMaxSubSquare(matrix):
    R = len(matrix)
    C = len(matrix[0])

    S = [[0 for k in range(C)] for l in range(R)]

    for i in range(1, R):
        for j in range(1, C):
            if(matrix[i][j] == 1):
                S[i][j] = min(S[i][j - 1], S[i-1][j], S[i - 1][j - 1]) + 1

    sMax = S[0][0]
    iMax = 0
    jMax = 0

    for i in range(R):
        for j in range(C):
           if sMax < S[i][j]:
               sMax = S[i][j]
               iMax = i
               jMax = j              

    print("Maximum size sub-matrix is: ")
    for i in range(iMax, iMax - sMax, -1):
        for j in range(jMax, jMax - sMax, -1):
            print(matrix[i][j], end=" ")
        print("")               

M = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]
 
printMaxSubSquare(M)        