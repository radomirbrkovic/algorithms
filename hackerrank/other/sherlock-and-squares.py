# Sherlock and Squares https://www.hackerrank.com/challenges/sherlock-and-squares/problem
import math


def squares(a, b):
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return int(count)


print squares(3, 9)        

print squares(17, 24)  

