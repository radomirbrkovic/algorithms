# Funny String https://www.hackerrank.com/challenges/funny-string/problem


def funnyString(s):
    r = s[::-1]
    for i in range(0, len(s) - 2):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(r[i]) - ord(r[i + 1])):
            return "Not Funny"
        
    return "Funny"    
    

print funnyString("acxz")
print funnyString("bcxz")