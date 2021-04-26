# Tiling Problem https://www.geeksforgeeks.org/tiling-problem/

def getNoOfWays(n):
    if n >= 0 and n <= 1:
        return n

    return getNoOfWays(n-1) + getNoOfWays(n - 2)

print(getNoOfWays(4))    #3    
print(getNoOfWays(3))    #2    