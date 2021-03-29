# The Full Counting Sort https://www.hackerrank.com/challenges/countingsort4/problem

def countSort(arr):
    result = [[] for i in range(100)]

    # first half of interation
    for i in range (n // 2):
        result[int(arr[i][0])].append('-')

    # second part of interation
    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])

    # printing result
    for string in result:
        if string:
            print(*string, end=' ')    