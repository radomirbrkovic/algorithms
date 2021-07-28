# Find minimum difference between any two elements https://www.geeksforgeeks.org/find-minimum-difference-pair/
import sys

def findMinDiff(arr) :
    diff = sys.maxsize
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(arr[i] - arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
    return diff

arr = [1, 5, 3, 19, 18, 25]    

print("Minimum difference is ", findMinDiff(arr))