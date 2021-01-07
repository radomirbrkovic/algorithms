# Equalize the Array https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    items = list(set(arr))
    maxRepetition = 0

    for i in items:
        count = arr.count(i)

        if count > maxRepetition:
            maxRepetition = count

    return len(arr) - maxRepetition


print equalizeArray([3, 3, 2, 1, 3])    

