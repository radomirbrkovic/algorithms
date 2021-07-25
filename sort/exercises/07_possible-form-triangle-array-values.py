# Possible to form a triangle from array values https://www.geeksforgeeks.org/possible-form-triangle-array-values/

def isPossibleTriangle (arr , N):
    if N < 3:
        return False
     
    arr.sort()
     
    for i in range(N - 2):
        if arr[i] + arr[i + 1] > arr[i + 2]:
            return True
 
# Driver Code
arr = [5, 4, 3, 1, 2]
N = len(arr)
print("Yes" if isPossibleTriangle(arr, N) else "No")