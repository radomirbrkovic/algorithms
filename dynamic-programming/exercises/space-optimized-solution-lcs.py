# A Space Optimized Solution of LCS https://www.geeksforgeeks.org/space-optimized-solution-lcs/

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    l = [[0 for i in range(n+1)] for j in range(2)] 

    bi = bool 
    for i in range(m):
        bi = i&1

        for j in range(n+1):
            if i == 0 or j == 0:
                l[bi][j] = 0
            elif X[i] == Y[j - 1]:
                l[bi][j] = l[1- bi][j - 1] + 1
            else:
                l[bi][j] = max(l[1 - bi][j], l[bi][j - 1])

    return l[bi][n]

X = "AGGTAB"
Y = "GXTXAYB"
 
print("Length of LCS is", lcs(X, Y))                    

