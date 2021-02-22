# Chocolate Feast https://www.hackerrank.com/challenges/chocolate-feast/problem


def chocolateFeast(n, c, m):
    count = n // c
    wrappers = count

    while wrappers >= m:
        count += wrappers // m
        wrappers = (wrappers % m) + (wrappers // m)



    return count



print chocolateFeast(10, 2, 5)    
print chocolateFeast(12, 4, 4)    
print chocolateFeast(6, 2, 2)    