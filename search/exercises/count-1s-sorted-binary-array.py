# Count 1’s in a sorted binary array https://www.geeksforgeeks.org/count-1s-sorted-binary-array/

def countOnes(arr,low,high):
     
    if high>=low:
        mid = low + (high-low)//2
        if ((mid == high or arr[mid+1]==0) and (arr[mid]==1)):
            return mid+1
             
        if arr[mid]==1:
            return countOnes(arr, (mid+1), high)
             
    
        return countOnes(arr, low, mid-1)

    return 0
    
arr=[1, 1, 1, 1, 0, 0, 0]
print ("Count of 1's in given array is",countOnes(arr, 0 , len(arr)-1))        