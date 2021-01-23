# Sherlock and Array https://www.hackerrank.com/challenges/sherlock-and-array/problem


def balancedSums(arr):
    n = len(arr)
    s = sum(arr)
    l = 0

    for x, i in zip(arr, range(n)):
        if s - x - l - l == 0:
            return "YES"
        l += x

    return "NO"         



print balancedSums([1, 2, 3])
print balancedSums([1, 2, 3, 3])
print balancedSums([1, 1, 4, 1, 1])
print balancedSums([2, 0, 0, 0])
print balancedSums([0, 0, 2, 0])