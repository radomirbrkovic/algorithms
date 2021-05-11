# Check if all rows of a matrix are circular rotations of each other https://www.geeksforgeeks.org/check-rows-matrix-circular-rotations/

def isPermutedMatrix(matrix):
    n = len(matrix[0])
    strCat = ""

    for i in range(n):
        strCat = strCat + "-" + str(matrix[0][i])

    strCat = strCat + strCat

    for i in range(1, n):
        currentStr = ""

        for j in range(n):
            currentStr = currentStr + "-"+ str(matrix[i][j])

        if strCat.find(currentStr) :
            return True

    return False                

if __name__ == "__main__" :
    mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]
     
    if (isPermutedMatrix(mat)):
        print("Yes")
    else :
        print("No")    