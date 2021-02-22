# Number Line Jumps https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:
        return "YES"
    else:
        return 'NO'             



print kangaroo(0, 3, 4, 2)

print kangaroo(0, 2, 5, 3)

print kangaroo(21, 6, 47, 3)