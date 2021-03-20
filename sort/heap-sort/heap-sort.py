import random

def heapify(arr, n, i):
    largest = i # Initialize the largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check does left child of the root exist and is it greater then root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Check does right child of the root exist and is it greater then root
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        #Heapify the root
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # one by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 

    return arr


print (heapSort(random.sample(range(1, 500), 200)))

    