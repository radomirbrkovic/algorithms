# Maximum Sum Increasing Subsequence | DP-14 https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

def getMaxSum(arr):
    n = len(arr)
    max = 0
    msis = [x for x in arr]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]

    for i in range(n):
        if max < msis[i]:
            max = msis[i]

    return max

arr = [1, 101, 2, 3, 100, 4, 5]
print("Sum of maximum sum increasing " +
                     "subsequence is " +
                  str(getMaxSum(arr)))                        