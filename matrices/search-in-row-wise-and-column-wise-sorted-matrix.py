# Search in a row wise and column wise sorted matrix https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

def search(matrix, x):
    n = len(matrix)
    if n == 0:
        return -1


    for i in range(n):
        for j in range(n):
            if(matrix[i][j] == x):
                print("Element found at (", i+1, ",", j+1, ")")
                return 1   

    print(" Element not found")
    return 0            

matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
    ] 

search(matrix, 29)    