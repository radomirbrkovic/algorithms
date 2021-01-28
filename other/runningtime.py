# Running Time of Algorithms https://www.hackerrank.com/challenges/runningtime/problem


def runningTime(arr):
    result = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j
        while i > 0 and arr[i-1] > key:
            arr[i] = arr[i-1]
            result += 1
            i -=1
         
        arr[i] = key
         
    return result


print runningTime([2, 1, 3, 1, 2])