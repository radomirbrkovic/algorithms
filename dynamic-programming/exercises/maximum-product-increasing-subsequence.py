# Maximum product of an increasing subsequence  https://www.geeksforgeeks.org/maximum-product-increasing-subsequence/
def getMaxProduct(arr):
    n = len(arr)
    msis = [x for x in arr]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and msis[i] < msis[j] * arr[i]:
                msis[i] = msis[j] * arr[i]

    return max(msis)


print(getMaxProduct([3, 100, 4, 5, 150, 6]))