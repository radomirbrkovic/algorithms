
def bubbleSortRecursive(last, n = None):
    
    if n is None:
        n = len(list)

    if n == 1:
        return 

    # One pass of bubble sort. After
    # this pass, the largest element
    # is moved (or bubbled) to end.  
    for i in range(n - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]

    # Largest element is fixed,
    # recur for remaining array     
    bubbleSortRecursive(list, n - 1)


list = [25, 21, 22, 24, 23, 27, 26]
bubbleSortRecursive(list)

print list