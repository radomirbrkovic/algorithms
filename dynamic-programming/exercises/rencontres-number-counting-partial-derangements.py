# Rencontres Number (Counting partial derangements) https://www.geeksforgeeks.org/rencontres-number-counting-partial-derangements/

def binomialCoeff(n, k):
    if(k == 0 or k == n):
        return 1

    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)


def rencontresNumber(n, m):
    if(n == 0 and m == 0):
        return 1

    if(n == 1 and m == 0):
        return 0

    if(m == 0):
        return((n - 1) * (rencontresNumber(n -1, 0) + rencontresNumber(n - 2, 0)))

    return (binomialCoeff(n, m) * rencontresNumber(n - m, 0))                

print(rencontresNumber(7, 2))