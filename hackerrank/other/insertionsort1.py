# Insertion Sort - Part 1 https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    key = arr[-1]
    i = n - 1

    while i > 0 and arr[i-1] > key:
        arr[i] = arr[i-1]
        print(*arr)

        i -=1

    arr[i] = key
    print(*arr)    
  


insertionSort1(5, [1, 2, 4, 5, 3])
insertionSort1(5, [2, 4, 6, 8, 3])