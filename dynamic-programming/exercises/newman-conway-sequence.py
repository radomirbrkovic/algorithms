# Newman-Conway Sequence https://www.geeksforgeeks.org/newman-conway-sequence/

def getNewmanConway(n):

    if n == 1 or n == 2:
        return 1

    return getNewmanConway(getNewmanConway(n-1)) + getNewmanConway(n - getNewmanConway(n - 1))


print(getNewmanConway(2)) #1
print(getNewmanConway(10)) #6