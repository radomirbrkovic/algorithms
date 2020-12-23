# Picking Numbers https://www.hackerrank.com/challenges/picking-numbers/problem
from collections import defaultdict

def pickingNumbers(arr):
    d = defaultdict(int)
    r_val = 0
    for val in arr:
        d[val] += 1
        r_val = max(r_val, d[val]+d[val+1], d[val]+d[val-1])
 
    return r_val     
                 

#print pickingNumbers([1, 2, 2, 3, 1, 2])

print pickingNumbers([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4])