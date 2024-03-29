# Search in an almost sorted array https://www.geeksforgeeks.org/search-almost-sorted-array/

def binarySearch(arr, l, r, x):
  
    if (r >= l):
          
        mid = int(l + (r - l) / 2)
          
        if (arr[mid] == x): return mid
        if (mid > l and arr[mid - 1] == x): 
            return (mid - 1)
        if (mid < r and arr[mid + 1] == x):
            return (mid + 1)
              
        
        if (arr[mid] > x):
            return binarySearch(arr, l, mid - 2, x)
          
        
        return binarySearch(arr, mid + 2, r, x)
  
    
    return -1

arr = [3, 2, 10, 4, 40]
n = len(arr)
x = 4
result = binarySearch(arr, 0, n - 1, x)
if (result == -1): 
    print("Element is not present in array") 
else:
    print("Element is present at index", result)    