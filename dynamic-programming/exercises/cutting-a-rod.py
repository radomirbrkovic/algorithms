# Cutting a Rod | DP-13 https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

import sys

def cutRod(price, n):
    if n <= 0:
        return 0

    maxVal = -sys.maxsize
    for i in range(n):
        maxVal = max(maxVal, price[i] + cutRod(price, n - i - 1))

    return maxVal

if __name__=="__main__":
    # Driver code
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    print("Maximum Obtainable Value is", cutRod(arr, len(arr)))