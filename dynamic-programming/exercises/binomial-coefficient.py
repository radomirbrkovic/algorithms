# Binomial Coefficient | DP-9 https://www.geeksforgeeks.org/binomial-coefficient-dp-9/

def binomialCoefficient(n, k):

    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1

    return binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1, k)

for i in range(1, 10):
    print("Value of binomialCoefficient(%d,%d) is %d" %(i+5, i, binomialCoefficient(i+5, i)))