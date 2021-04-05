# Weighted Uniform Strings https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    result = []
    d = {}
    weight = 0

    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            weight = ord(s[i]) - ord('a') + 1
        else:
            weight += ord(s[i]) - ord('a') + 1

        d[weight] = 1

    for q in queries:
        result.append("Yes" if q in d else "No")

    return result    



print(weightedUniformStrings('aaabbbbcccddd', [5, 9, 7, 8, 12, 5]))   