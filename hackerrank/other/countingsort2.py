# Counting Sort 2 https://www.hackerrank.com/challenges/countingsort2/problem

def countingSort(arr):
    count = [0] * (max(arr) + 1)

    for  num in arr:
        count[num] += 1

    sortedArray = []
    for  i in range(len(count)):
        while count[i] != 0:
            count[i] -= 1
            sortedArray.append(i)

    return sortedArray            