def linearSearch(array, item):
    index = 0
    result = False

    while index < len(array) and result == False: 
        if array[index] == item:
            result = True
        else:
            index += 1    

    return result


print linearSearch([10, 11, 5, 7, 1, 9, 45, 32, 21], 7) #True    
print linearSearch([10, 11, 5, 7, 1, 9, 45, 32, 21], 99) #False    