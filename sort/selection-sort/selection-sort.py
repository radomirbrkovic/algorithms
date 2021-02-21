def SelectionSort(list):
    for fillSlot in range(len(list) - 1, 0, -1):
        maxIndex = 0
        for location in range(1, fillSlot +1):
            if list[location] > list[maxIndex]:
                maxIndex = location
        list[fillSlot], list[maxIndex] = list[maxIndex], list[fillSlot]

    return list           

print SelectionSort([20, 17, 26, 11, 23, 21, 13, 19, 16])    