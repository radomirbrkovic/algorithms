# String Construction https://www.hackerrank.com/challenges/string-construction/problem

def stringConstruction(s):
    result = []

    for i in range(len(s)):
         if not s[i] in result:
             result.append(s[i])   

    return len(result)

print stringConstruction('abcd') # 4
print stringConstruction('abab') # 2