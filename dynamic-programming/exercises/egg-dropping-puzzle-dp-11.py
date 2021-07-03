# Egg Dropping Puzzle | DP-11 https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

import sys

def eggDrop(n, k):

    if( k == 0 or k == 1 or n == 1):
        return k

    min = sys.maxsize

    for x in range(1, k + 1):
        res = max(eggDrop(n - 1, x - 1), eggDrop(n, k - x))

        if res < min:
            min = res
    
    return min + 1        

print("Minimum number of trials in worst case with",
           2, "eggs and", 10, "floors is", eggDrop(2, 10))