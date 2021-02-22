# Between Two Sets https://www.hackerrank.com/challenges/between-two-sets/problem
# https://www.mathblog.dk/hackerrank-between-two-sets-in-python/

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b

def lcm(a, b):
    return a * b  // gcd(a, b)

def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm, min_gcd+1, max_lcm) if min_gcd % x == 0])
 
    return count    

print getTotalX([2, 4], [16, 32, 96])    