# Minimum Absolute Difference in an Array https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem 


def minimumAbsoluteDifference(arr):
    arr.sort()
    min = abs(arr[0] - arr[1])

    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i + 1]) < min:
            min = abs(arr[i] - arr[i + 1])
    return min

print minimumAbsoluteDifference([3, -7, 0]) #3     
print minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) #1     
print minimumAbsoluteDifference([1, -3, 71, 68, 17]) #3     