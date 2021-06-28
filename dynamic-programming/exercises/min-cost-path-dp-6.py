# Min Cost Path | DP-6 https://www.geeksforgeeks.org/min-cost-path-dp-6/

import sys

def minCost(matrix, m, n):
    if n < 0 or m < 0:
        return sys.maxsize
    elif m == 0 and n == 0:
        return matrix[m][n]
    else:
        return matrix[m][n] + myMin(minCost(matrix, m - 1, n -1), minCost(matrix, m -1, n), minCost(matrix, m, n - 1))        

def myMin(x, y, z):
     if x < y:
         return x if x < z else z
     else:
         return y if y < z else z

matrix= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(minCost(matrix, 2, 2))         


