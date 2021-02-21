def ShellSort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            tmp = list[i]
            j = i

            while j >= distance and list[j - distance] > tmp:
                list[j] = list[j - distance]
                j = j - distance

            list[j] = tmp

        distance = distance // 2

    return list


print ShellSort([20, 17, 26, 11, 23, 21, 13, 19, 16])