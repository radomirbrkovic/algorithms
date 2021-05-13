# Find distinct elements common to all rows of a matrix https://www.geeksforgeeks.org/find-distinct-elements-common-rows-matrix/

def findCommonElements(matrix):
    n = len(matrix)
    result = matrix[0]

    for i in range(1, n):
        for x in result:
            if not x in matrix[i]:
                result.remove(x)

    result.sort()
    return result             

if __name__ == "__main__" :
    mat = [[12, 1, 14, 3, 16],
       [14, 2, 1, 3, 35],
       [14, 1, 14, 3, 11],
       [14, 25, 3, 2, 1],
       [1, 18, 3, 21, 14]]

    print(findCommonElements(mat))
