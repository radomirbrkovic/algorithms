# Counting sets of 1s and 0s in a binary matrix https://www.geeksforgeeks.org/counting-sets-of-1s-and-0s-in-a-binary-matrix/

def countSets(matrix):
    result = 0
    for i in range(len(matrix)):
        u = 0
        v = 0
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                u += 1
            else:
                v += 1

        result += pow(2, u) - 1 + pow(2, v) - 1

    for i in range(len(matrix[0])):
        u = 0
        v = 0
        for j in range(len(matrix)):
            if matrix[j][i]:
                u += 1
            else:
                v += 1

        result += pow(2, u) - 1 + pow(2, v) - 1    

    return result - (len(matrix) * len(matrix[0]))

matrix = [
    [1, 0, 1],
    [0, 1, 0]
    ]     


print(countSets(matrix))