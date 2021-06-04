# Check given matrix is magic square or not https://www.geeksforgeeks.org/check-given-matrix-is-magic-square-or-not/

def isMagicSquare(matrix):
    s = 0
    n = len(matrix)

    for i in range(n):
        s+= matrix[i][i]

    s2 = 0
    for i in range(n):
        s2 += matrix[i][n-i-1]


    if s != s2:
        return False

    for i in range(n):
        if sum(matrix[i]) != s:
            return False

    for i in  range(n):
        colSum = 0
        for j in range(n):
            colSum += matrix[j][i]

        if s != colSum:
            return False


    return True            


matrix = [ [ 2, 7, 6 ],
        [ 9, 5, 1 ],
        [ 4, 3, 8 ] ]
     
if (isMagicSquare(matrix)) :
    print( "Magic Square")
else :
    print( "Not a magic Square")
