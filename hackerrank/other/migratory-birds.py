# Migratory birds https://www.hackerrank.com/challenges/migratory-birds/problem
import operator

def migratoryBirds(arr):
    repl = {}

    for i in arr:
        if i in repl:
            repl[i] = repl[i] + 1
        else:
            repl[i] =  1

    return max(repl, key=repl.get)             

print migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])