# Max Min https://www.hackerrank.com/challenges/angry-children/problem


def maxMin(k, arr):
    n = len(arr)
    # Sorting the array.
    arr.sort()
    result = arr[k-1] - arr[0]
    for i in range(n-k+1):
        result = int(min(result, arr[i+k-1] - arr[i]))
   
    return result



print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30])) #20
print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200])) #3