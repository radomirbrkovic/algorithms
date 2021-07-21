# Given a sorted array and a number x, find the pair in array whose sum is closest to x https://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/

import sys

def printClosest(arr, x):
    n = len(arr)

    resL, resR = 0, 0

    l, r, diff = 0, n -1, sys.maxsize

    while r > l:
        if abs(arr[l] + arr[r] - x) < diff:
            resL = l
            resR = r
            diff =  abs(arr[l] + arr[r] - x)
        
        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1    

    print(f"The closest pair is {arr[resL]} and {arr[resR]}")


if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    x=54
    printClosest(arr, x)    