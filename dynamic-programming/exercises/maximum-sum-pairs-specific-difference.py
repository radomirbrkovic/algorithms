# Maximum sum of pairs with specific difference https://www.geeksforgeeks.org/maximum-sum-pairs-specific-difference/

def maxSumPairWithDifferenceLessThanK(arr, K):
    N = len(arr)
    arr.sort()

    dp = [0] * N

    dp[0] = 0

    for i in range(1, N):
        dp[i] = dp[i - 1]
        if(arr[i] - arr[i - 1] < K):
            if(i >= 2):
                dp[i] = max(dp[i], dp[i - 2] + arr[i] + arr[i - 1])
            else:
                dp[i] = max(dp[i], arr[i] + arr[i - 1])

    return dp[N - 1]                

arr = [3, 5, 10, 15, 17, 12, 9]
print(maxSumPairWithDifferenceLessThanK(arr, 4))