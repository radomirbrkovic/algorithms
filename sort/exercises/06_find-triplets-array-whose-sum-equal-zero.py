# Find all triplets with zero sum https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/

def findTriplets(arr):
    n = len(arr)
    found = False
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
             

    if (found == False):
        print(" not exist ")

arr = [0, -1, 2, -3, 1]
findTriplets(arr)