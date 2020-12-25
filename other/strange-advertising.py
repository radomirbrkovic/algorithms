# Viral Advertising https://www.hackerrank.com/challenges/strange-advertising/problem
import math


def viralAdvertising(n):
    result = 0
    total  = 0
    for i in range(1, n + 1):
        if i == 1:
            result = math.floor(5/2)
        else:
            result = math.floor(result * 3 / 2)

        total = total + result
    return int(total)      

print viralAdvertising(3)    