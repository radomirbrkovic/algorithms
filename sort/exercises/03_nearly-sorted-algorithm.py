# Sort a nearly sorted (or K sorted) array https://www.geeksforgeeks.org/nearly-sorted-algorithm/
from heapq import heappop, heappush, heapify

def print_array(arr: list):
    for elem in arr:
        print(elem, end=' ')

def sortK(arr: list,  k: int):
    n = len(arr)

    heap = arr[:k + 1]
    heapify(heap)

    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1
 
    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1


arr = [2, 6, 3, 12, 56, 8] 
sortK(arr, 3)

print('Following is sorted array')
print_array(arr)