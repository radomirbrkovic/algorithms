# Find a Fixed Point (Value equal to index) in a given array https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

def linearSearch(arr):
    for i in range(len(arr)):
        if arr[i] is i:
            return i

    return -1

print("Fixed Point is " + str(linearSearch([-10, -1, 0, 3, 10, 11, 30, 50, 100])))    