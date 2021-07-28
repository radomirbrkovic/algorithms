# Find Surpasser Count of each element in array https://www.geeksforgeeks.org/find-surpasser-count-of-each-element-in-array/

def findSurpasser(arr, n):
 
    for i in range(n):
        count = 0;
 
        for j in range (i + 1, n):
            if (arr[j] > arr[i]):
                count += 1
 
        print(count, end = " ")

def printArray(arr, n):
 
    for i in range(n):
        print(arr[i], end = " ")    

arr = [2, 7, 5, 3, 0, 8, 1 ]
n = len(arr)
 
print("Given array is")
printArray(arr , n)
 
print("\nSurpasser Count of array is");
findSurpasser(arr , n)            