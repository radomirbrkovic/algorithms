# Sequence Equation https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p):
    result = []

    n = len(p)

    for i in range(1, n+1):
        result.append(p.index(p.index(i)+1) + 1)

    return result

print permutationEquation([4, 3, 5, 1, 2])