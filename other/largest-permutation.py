# Largest Permutation https://www.hackerrank.com/challenges/largest-permutation/problem

def largestPermutation(k, arr):
    maxcur = max(arr)
    positions = {}

    for ind in range(len(arr)):
        positions[arr[ind]] = ind

    for ind in range(len(arr)):
        if k == 0:
            break

        if arr[ind] == maxcur:
            maxcur -= 1    

        if arr[ind] < maxcur:
            mind = positions[maxcur]
            positions[maxcur], positions[arr[ind]] = positions[arr[ind]], positions[maxcur]
            arr[ind], arr[mind] = arr[mind], arr[ind]
            maxcur -= 1
            k -= 1


    return arr



print largestPermutation(1, [4, 2, 3, 5, 1]) #5 2 3 4 1
print largestPermutation(1, [2, 1, 3]) #3 1 2