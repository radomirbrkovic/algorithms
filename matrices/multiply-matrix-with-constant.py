# Example of multiplying matrix by given constant (scalar multiplication)

def multiplayMatrixByConstant(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= n


if __name__ == "__main__" :
    matrix = [ 
        [1, 3, 5], 
        [2, 6, 9], 
        [3, 6, 9]]

    multiplayMatrixByConstant(matrix, 5)
    print(matrix)

