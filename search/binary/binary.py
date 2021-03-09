def binarySearch(array, item):
    first = 0 
    last = len(array) - 1
    result = False

    while first <= last and not result:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            result = True
        else:
            if item < array[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return result                     



print binarySearch([1, 3, 5, 7, 8, 9, 13, 17], 7) # True    
print binarySearch([1, 3, 5, 7, 8, 9, 13, 17], 16) # False    