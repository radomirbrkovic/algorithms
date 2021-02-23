# Smart Number https://www.hackerrank.com/challenges/smart-number/problem

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val**2 == 1:
        return True
    return False


print is_smart_number(1) #True
print is_smart_number(2) #False
print is_smart_number(7) #False
print is_smart_number(169) #True

