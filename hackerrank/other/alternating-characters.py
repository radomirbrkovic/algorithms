# Alternating Characters https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    n = len(s)
    target = s[0]
    result = 0

    for i in range(1, n):
        if target == s[i]:
            result += 1
        else:
            target = s[i]

    return result            


print alternatingCharacters('AAAA')    
print alternatingCharacters('BBBBB')    
print alternatingCharacters('ABABABAB')    
print alternatingCharacters('BABABA')    
print alternatingCharacters('AAABBB')    
