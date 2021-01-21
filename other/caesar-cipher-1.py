# Caesar Cipher https://www.hackerrank.com/challenges/caesar-cipher-1/problem
from string import lowercase, uppercase

def caesarCipher(s, k):
    result = []
    for c in s:
        if c in lowercase:
            idx = (lowercase.index(c) + k) % 26
            result.append(lowercase[idx])
        elif c in uppercase:
            idx = (uppercase.index(c) + k) % 26
            result.append(uppercase[idx])
        else:
            result.append(c)
    return "".join(result)


print caesarCipher('middle-Outz', 2)