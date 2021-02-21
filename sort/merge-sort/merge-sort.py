def MergeSort(list):

    if len(list) > 1:
        mid = len(list) // 2 # splits list in half
        left = list[:mid]
        right = list[mid:]

        MergeSort(left)
        MergeSort(right)

        a = b = c = 0
    
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a += 1 
            else:
                list[c] = right[b]
                b += 1

            c += 1

        while a < len(left):
            list[c] = left[a]
            a+= 1
            c+= 1

        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1


    return list    


print MergeSort([44, 16, 83, 7, 67 , 21, 34, 46, 10])