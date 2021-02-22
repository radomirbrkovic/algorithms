# The Love-Letter Mystery https://www.hackerrank.com/challenges/the-love-letter-mystery/problem


def theLoveLetterMystery(s):
    count = 0
    n = len(s)

    for i in range(n//2):
        count += abs(ord(s[i]) - ord(s[n - 1 - i]))

    return count    

print theLoveLetterMystery('abc') #2
print theLoveLetterMystery('abcba') #0
print theLoveLetterMystery('abcd') #4
print theLoveLetterMystery('cba') #2
