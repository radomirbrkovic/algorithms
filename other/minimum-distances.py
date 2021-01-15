# Minimum Distances https://www.hackerrank.com/challenges/minimum-distances/problem


def minimumDistances(a):
    tempElements = {}
    distances = []

    for i, el in enumerate(a):
        if not tempElements.has_key(el):
            tempElements[el] = i
        else:
            distances.append(abs(i - tempElements[el]))
            del tempElements[el]     

    if not len(distances):
        return -1
    else:
        return min(distances)    


print minimumDistances([7, 1, 3, 4, 1, 7])    