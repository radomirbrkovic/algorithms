# Lily's Homework https://www.hackerrank.com/challenges/lilys-homework/problem

def lilysHomeworkHelper(arr, reverse = False):
    steps = 0

    arr = arr[:]

    sortedArr = sorted(arr, reverse=reverse)
    indexesByValue = {}

    for i, val in enumerate(arr):
        indexesByValue[val] = i

    for goodI, currentVal in enumerate(arr):
        sortedVal = sortedArr[goodI]
        badI = indexesByValue[sortedVal]

        if goodI != badI:
            arr[badI] = currentVal
            arr[goodI] = sortedVal
            steps += 1

            indexesByValue[currentVal] = badI


    return steps

def lilysHomework(arr):

    forwardCount = lilysHomeworkHelper(arr)
    reverseCount = lilysHomeworkHelper(arr, True)

    return min(forwardCount, reverseCount)


print lilysHomework([2, 5, 3, 1])