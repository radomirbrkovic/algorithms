# Gemstones https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    characters = {}

    for i in arr[0]:
        characters[i] = 0

    for i in arr:
        for (char, value) in characters.items():
            if char in i:
                characters[char] += 1

    result = 0
    n = len(arr)

    for (key, value) in characters.items(): 
        if value == n:
            result += 1

    return result                       


print gemstones(['abcdde', 'baccd', 'eeabg'])