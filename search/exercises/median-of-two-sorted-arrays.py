# Median of two sorted arrays of same size https://www.geeksforgeeks.org/median-of-two-sorted-arrays/

def getMedian( ar1, ar2):
    i = 0
    j = 0

    m1 = -1
    m2 = -1

    count = 0
    n = len(ar1)

    while count < n + 1:
        count += 1

        if i == n:
            m1 = m2
            m2 = ar2[0]
            break
        elif j == n:
            m1 = m2
            m2 = ar1[0]
            break

        if ar1[i] <= ar2[j]:
            m1 = m2 
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2 
            m2 = ar2[j]
            j += 1

    return (m1 + m2)/2        

ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
if  len(ar1) == len(ar2):
    print("Median is ", getMedian(ar1, ar2))
else:
    print("Doesn't work for arrays of unequal size")