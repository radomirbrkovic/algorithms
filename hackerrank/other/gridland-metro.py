# Gridland Metro https://www.hackerrank.com/challenges/gridland-metro/problem

def gridlandMetro(n, m, k, track):
    track.sort( key = lambda track:min(track[1], track[2]))
    runningTotal = 0
    lastColEndByRows = {}

    for row, colStart, colEnd in track:
        if colEnd < colStart :
            colStart, colEnd = colEnd, colStart

        if not lastColEndByRows.get(row):
            lastColEndByRows[row] = colEnd
            runningTotal += colEnd - colStart + 1
        else:
            lastColEndByRow = lastColEndByRows[row]

            if lastColEndByRow < colStart:
                lastColEndByRows[row] = colEnd
                runningTotal += colEnd - colStart + 1
            elif lastColEndByRow < colEnd:
                lastColEndByRows[row] = colEnd
                runningTotal += colEnd - lastColEndByRow 

            else:
                continue    


    return n * m -  runningTotal        



print gridlandMetro(4, 4, 3 [
        [2, 2, 3],
        [3, 1, 4],
        [4, 4, 4],
])    