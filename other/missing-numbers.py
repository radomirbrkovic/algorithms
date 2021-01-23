# Missing Numbers https://www.hackerrank.com/challenges/missing-numbers/problem

def missingNumbers(arr, brr):
    aDi = {}

    bDi = {}

    for i in arr:
        if i in aDi:
            aDi[i] += 1
        else:
            aDi[i] = 1

    for i in brr:
        if i in bDi:
            bDi[i] += 1
        else:
            bDi[i] = 1
            

    result = []

    for (i, count) in bDi.items():
        if i not in aDi or aDi[i] < count:
            result.append(i)

    return sorted(result)                             

print missingNumbers(
    [203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
    [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
)