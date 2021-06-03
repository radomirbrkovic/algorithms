# Longest Common Subsequence | DP-4 https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 +lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X,Y, m-1, n))         


if __name__=="__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print( "Length of LCS is ", lcs(X , Y, len(X), len(Y)))