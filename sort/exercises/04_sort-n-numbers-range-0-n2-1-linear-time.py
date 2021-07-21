# Sort n numbers in range from 0 to n^2 – 1 in linear time https://www.geeksforgeeks.org/sort-n-numbers-range-0-n2-1-linear-time/

def countSort(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * n

    for i in range(n):
        count[ (arr[i] // exp) % n ] += 1

    for i in range(1, n):
        count[i] += count[i - 1]
 
    for i in range(n - 1, -1, -1):
 
        output[count[ (arr[i] // exp) % n] - 1] = arr[i]
        count[(arr[i] // exp) % n] -= 1
 
    for i in range(n):
        arr[i] = output[i]    

def sort(arr, n) :
    countSort(arr,  1)
    countSort(arr, n)       


if __name__ =="__main__":
     
   
    arr = [40, 12, 45, 32, 33, 1, 22]
    n = len(arr)
    print("Given array is")
    print(*arr)
     
    sort(arr, n)
     
    print("Sorted array is")
    print(*arr)