# Find the row with maximum number of 1s https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/

def getRowWithMax1s(matrix):
    max = 0
    row = 0
    for i in range(len(matrix)):
        tmpCount = sum(matrix[i])

        if tmpCount > max:
            max = tmpCount
            row = i

    return row        

if __name__ == "__main__" :
    mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
      getRowWithMax1s(mat))