# Pangrams https://www.hackerrank.com/challenges/pangrams/problem

lowerCase = "abcdefghijklmnopqrstuvwxyz"

def pangrams(s):
    checked = 0

    for i in lowerCase:
        if i in s or i.upper() in s:
            checked += 1

    if len(lowerCase) == checked:
        return "pangram"
    else:
        return "not pangram"            



print pangrams('We promptly judged antique ivory buckles for the next prize')
print pangrams('We promptly judged antique ivory buckles for the prize')

