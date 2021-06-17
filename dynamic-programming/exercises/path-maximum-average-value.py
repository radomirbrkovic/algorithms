# Path with maximum average value https://www.geeksforgeeks.org/path-maximum-average-value/

def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0 for i in range(n +1)] for j in range(n+1)]

    dp[0][0]= matrix[0][0]

    for i in range (1, n):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for i in range (1, n):
        dp[0][i] = dp[0][i - 1] + matrix[0][i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[n - 1][n - 1] / (2 * n - 1)        


matrix = [[1, 2, 3],
        [6, 5, 4],
        [7, 3, 9]]

print(maxAverageOfPath(matrix))        