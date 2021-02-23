# Anagram https://www.hackerrank.com/challenges/anagram/problem


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        left={}
        right={}

        for i in range(len(s) // 2):
            if s[i] in left:
                left[s[i]] += 1
            else:
                left[s[i]] = 1

        for i in range(len(s) // 2, len(s)):
            if s[i] in right:
                right[s[i]] += 1
            else:
                right[s[i]] = 1

        counter = 0

        for i, v in right.items():
            if i not in left:
                counter += v
            elif v > left[i]:
                counter += v - left[i]

        return counter            


print anagram('aaabbb') #3    
print anagram('ab') #1    
print anagram('abc') # -1    
print anagram('mnop') # 2    
print anagram('xyyx') # 0  
print anagram('xaxbbbxx') # 1  