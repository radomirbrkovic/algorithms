# Dynamic Array https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]

    lastAnswer = 0
    result = []

    for q, x, y in queries:
        idx = (x ^ lastAnswer) % n 
        if q == 1:
            seq[idx].append(y)
        else:
            v = y % len(seq[idx])
            lastAnswer = seq[idx][v]
            result.append(lastAnswer)

    return result        