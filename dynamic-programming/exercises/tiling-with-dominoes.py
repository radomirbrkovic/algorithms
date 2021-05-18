# Tiling with Dominoes https://www.geeksforgeeks.org/tiling-with-dominoes/

def countWays(n):
    A = [-1 for x in range(n+1)]
    B = [-1 for x in range(n+1)]

    A[0] = 1
    A[1] = 0
    B[0] = 0
    B[1] = 1
    for i in range(2, n+1):
        
        A[i] = A[i - 2] + 2 * B[i-1]
        B[i] = A[i -1] + B[i-2]
    return A[n]     
    
         
print(countWays(8))


