# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen


def diagonalDifference(arr):

    sumX = 0
    sumY = 0

    for i in range(len(arr)):
        sumX += arr[i][i]
        sumY += arr[i][(len(arr) - 1) - i]

    return abs(sumX - sumY)    



matrix = [
    [11, 2, 4],
    [4, 5 , 6],
    [10, 8, -12]
]

print diagonalDifference(matrix)