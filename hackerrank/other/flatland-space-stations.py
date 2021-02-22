# Flatland Space Stations https://www.hackerrank.com/challenges/flatland-space-stations/problem


def flatlandSpaceStations(n, c):
    answer = 0
    c.sort()

    for i in range(1, len(c)):
        answer = max(answer, (c[i] - c[i-1]) // 2)

    answer = max(answer, c[0], n - 1 - c[-1])

    return answer    

print flatlandSpaceStations(5, [0, 4]) # 2   
print flatlandSpaceStations(6, [0, 1, 2, 4, 3, 5]) # 0   