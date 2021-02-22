# Two Strings https://www.hackerrank.com/challenges/two-strings/problem

def twoStrings(s1, s2):
    
    if len(s2) < len(s1):
        s1, s2= s2, s1

    for i in range(len(s1)):
        if s1[i] in s2:
            return 'YES'

    return 'NO'        


print twoStrings('hello', 'world') # YES
print twoStrings('hi', 'world') # NO