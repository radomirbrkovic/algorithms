# Find the smallest and second smallest elements in an array https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/

import sys
 
def print2Smallest(arr):

    arrSize = len(arr)

    if arrSize < 2:
        print("Invalid Input")
        return

    first = second = sys.maxsize
    for i in range(arrSize):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second and arr[i] != first:
            second = arr[i]

    if (second == sys.maxsize):
        print ("No second smallest element")
    else:
        print (f'The smallest element is {first} and  second smallest element is {second}')    

arr = [12, 13, 1, 10, 34, 1]
print2Smallest(arr)