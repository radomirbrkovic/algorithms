# Find the Missing Number https://www.geeksforgeeks.org/find-the-missing-number/


def getMissingNumber(array):
    n = len(array)
    return ((n+1) * (n+2) / 2 ) - sum(array) 

print(getMissingNumber([1, 2, 4, 5, 6]))    