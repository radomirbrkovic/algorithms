# Example of multiplying two matrices (dot product)

def multiplyMatrices(A, B):
    
    if len(A) != len(B[0]):
        raise Exception("Number of columns from firs matrix must be equal with the number of rows from secont matrix") 

    result = []
    for i in range(len(A)):
        tmp = []    
        for j in range(len(A[i])):
            tmp.append(A[i][j] * B[j][i])

        result.append(sum(tmp))

    return result

if __name__ == "__main__" :
    matA = [
        [1, 2 , 3],
        [4, 5 , 6],
        ]
    matB = [
            [7, 8],
            [9, 10],
            [11, 12],
        ]
    print(multiplyMatrices(matA, matB))                    
