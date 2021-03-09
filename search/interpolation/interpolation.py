def interpolationSearch(array, item):
    idx0 = 0
    idxN = len(array) - 1

    result = False
    while idx0 <= idxN and item >= array[idx0] and item <= array[idxN]:
        midpoint = idx0 + int(((float (idxN - idx0) / (array[idxN]  - array[idx0])) * (item - array[idx0])))

        if array[midpoint] == item:
            result = True
            return result

        if array[midpoint] < item:
            idx0 = midpoint + 1    


    return result


print interpolationSearch([1, 3, 5, 7, 8, 9, 13, 17], 7) # True    
print interpolationSearch([1, 3, 5, 7, 8, 9, 13, 17], 16) # False        