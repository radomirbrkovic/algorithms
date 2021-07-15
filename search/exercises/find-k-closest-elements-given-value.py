# Find k closest elements to a given value https://www.geeksforgeeks.org/find-k-closest-elements-given-value/

def findCrossOver(arr, low, high, x) :
 
    if (arr[high] <= x) :
        return high
         
    if (arr[low] > x) :
        return low
     
    mid = (low + high) // 2 
    
    if (arr[mid] <= x and arr[mid + 1] > x) :
        return mid
     
    
    if(arr[mid] < x) :
        return findCrossOver(arr, mid + 1, high, x)
     
    return findCrossOver(arr, low, mid - 1, x)

def printKclosest(arr, x, k, n) :
     
    l = findCrossOver(arr, 0, n - 1, x)
    r = l + 1
    count = 0
              
 
    if (arr[l] == x) :
        l -= 1
 
    while (l >= 0 and r < n and count < k) :
         
        if (x - arr[l] < arr[r] - x) :
            print(arr[l], end = " ")
            l -= 1
        else :
            print(arr[r], end = " ")
            r += 1
        count += 1
 
    while (count < k and l >= 0) :
        print(arr[l], end = " ")
        l -= 1
        count += 1
 
    while (count < k and r < n) :
        print(arr[r], end = " ")
        r += 1
        count += 1    

if __name__ == "__main__" :
 
    arr =[12, 16, 22, 30, 35, 39, 42,
              45, 48, 50, 53, 55, 56]
                 
    n = len(arr)
    x = 35
    k = 4
     
    printKclosest(arr, x, 4, n)        