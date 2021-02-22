# Closest Numbers https://www.hackerrank.com/challenges/closest-numbers/problem
import sys

def closestNumbers(arr):
    output = []
    minDiff = sys.maxsize
    arr.sort()

    for i in range(1, len(arr)):
        d = abs(arr[i - 1] - arr[i])
        if d < minDiff:
            minDiff = d
            output  = [arr[i -1], arr[i]]
        elif d == minDiff:
            output.extend([arr[i-1], arr[i]])
    return output


print closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854])                
print closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470])