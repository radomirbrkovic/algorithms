def InsertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        nextElement = array[i]

        while (array[j] > nextElement) and j >= 0:
            array[j+1] = array[j]
            j = j -1

        array[j+1] = nextElement
    
    return array         


print InsertionSort([25, 21, 22, 24, 23, 27, 26])    