# Palindrome Index https://www.hackerrank.com/challenges/palindrome-index/problem

def palindromeIndex(s):
    if s == s[::-1]:
        return -1

    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-1-i
            elif s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i

    return -1                   

print palindromeIndex('aaab') # 3    
print palindromeIndex('baa') # 0    
print palindromeIndex('aaa') # -1    