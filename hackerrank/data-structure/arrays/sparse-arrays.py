# Sparse Arrays https://www.hackerrank.com/challenges/sparse-arrays/problem

def matchingStrings(strings, queries):
    counter = {}

    for i in strings:
        if i in queries:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

    result = []

    for i in range(len(queries)):
        if queries[i] in counter:
            result.append(counter[queries[i]])
        else:
            result.append(0)

    return result                            

print(matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']))    