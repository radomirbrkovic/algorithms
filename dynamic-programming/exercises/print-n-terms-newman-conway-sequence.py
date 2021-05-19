# Print n terms of Newman-Conway Sequence https://www.geeksforgeeks.org/print-n-terms-newman-conway-sequence/


def getNewmanConway(n):

    if n == 1 or n == 2:
        return 1

    return getNewmanConway(getNewmanConway(n-1)) + getNewmanConway(n - getNewmanConway(n - 1))


def printNewmanConwaySequence(n):
    for i in range(1, n+1):
        print(getNewmanConway(i), end=" ")

    print("")

printNewmanConwaySequence(13)
printNewmanConwaySequence(20)