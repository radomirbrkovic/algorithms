# XOR Strings https://www.hackerrank.com/challenges/strings-xor/problem

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

print strings_xor('10101', '00101') #10000

