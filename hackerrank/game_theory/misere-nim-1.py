# Misere Nim https://www.hackerrank.com/challenges/misere-nim-1/problem
from functools import reduce


def misereNim(s):
    if set(s) == {1}:
        if len(s)%2 == 0:
            return 'First'
        else:
            return 'Second'

    res = reduce((lambda x, y: x ^ y), s)
    if res == 0:
        return 'Second'
    else:
        return 'First'
  


print misereNim([1, 1]) # First    
print misereNim([2, 1, 3]) # Second    