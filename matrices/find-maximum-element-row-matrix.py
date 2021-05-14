# Find maximum element of each row in a matrix https://www.geeksforgeeks.org/find-maximum-element-row-matrix/

def getMaxELementFroMatrix(matrix):

    result = []

    for row in matrix:
        result.append(max(row))

    return result    

if __name__ == "__main__" : 
    a =  [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]

    print(getMaxELementFroMatrix(a))    