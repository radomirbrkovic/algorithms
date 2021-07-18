# Sort an array of 0s, 1s and 2s https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

def sort012(arr):
    lo = 0
    hi = len(arr) - 1
    mid = 0

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1

    return arr                   

def printArray(arr):
    for i in arr:
        print(i)     

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr = sort012(arr)
print("Array after segregation") 
printArray(arr)