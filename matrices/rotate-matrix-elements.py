# Rotate Matrix Elements https://www.geeksforgeeks.org/rotate-matrix-elements/

def rotateMatrix(matrix):
    
    if not len(matrix):
        return

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while left < right and top < bottom:
        prev = matrix[top +1][left]

        # move elements of top row none step right
        for i in range(left, right + 1):
            current = matrix[top][i]
            matrix[top][i] = prev
            prev = current

        top += 1

        #Move elements of rightmost column one step downwards
        for i in range(top, bottom +1):
            current = matrix[i][right]
            matrix[i][right] = prev
            prev = current

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left - 1, -1):
            current = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = current

        bottom -= 1 

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top - 1 , -1):
            current = matrix[i][left]
            matrix[i][left] = prev
            prev = current

        left += 1

    return matrix        

def printMatrix(mat):
    for row in mat:
        print(row)
 
if __name__ == "__main__": 
    matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
    ]
    printMatrix(matrix)
    matrix = rotateMatrix(matrix)
    # Print modified matrix
    printMatrix(matrix)
          