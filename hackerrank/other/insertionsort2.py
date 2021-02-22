# Insertion Sort - Part 2 https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort2(n, arr):
    for j in range(1, n):
        key = arr[j]
        i = j
        while i > 0 and arr[i - 1] > key:
            arr[i] = arr[i - 1]
            i -=1

        arr[i] = key
        print(*arr)    


insertionSort2(6, [1, 4, 3, 5, 6, 2])        