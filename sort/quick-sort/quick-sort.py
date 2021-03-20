import random

def partition(arr, low, high):
    pivot = arr[high]
    # Index of smaller element and indicates the 
    # right position of pivot found so far
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            i += 1 #increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    
    if low < high:
       # pi is partitioning index, arr[pi] is now at right place    
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  # Before pi
        quickSort(arr, pi + 1, high); # After pi



arr = random.sample(range(1, 500), 200)
quickSort(arr, 0, len(arr) - 1 )

print(arr)