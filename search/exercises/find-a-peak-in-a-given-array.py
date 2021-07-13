# Find a peak element https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

def findPeak(arr) :
    n = len(arr)
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
  

    for i in range(1, n - 1) :
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
             
# Driver code.
arr = [ 1, 3, 20, 4, 1, 0 ]
print("Index of a peak point is", findPeak(arr))