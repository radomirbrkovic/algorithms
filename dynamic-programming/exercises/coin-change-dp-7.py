# Coin Change | DP-7 https://www.geeksforgeeks.org/coin-change-dp-7/


def count(S, m, n):
    
    if n == 0:
        return 1
    elif n < 0:
        return 0

    if (m <= 0 and n >= 1):
        return 0

    return count(S, m - 1, n) + count(S, m, n - S[m-1])            

arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))
    