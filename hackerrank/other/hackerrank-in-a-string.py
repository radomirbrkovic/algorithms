# HackerRank in a String! https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def hackerrankInString(s):
    li = list(s)
    h = {'h': 1, 'a': 2, 'c':1, 'k':2, 'e':1, 'r':2, 'n':1}

    for c in h:
        if li.count(c) < h[c]:
            return "NO"

    return "YES"



print hackerrankInString("hereiamstackerrank")    
print hackerrankInString("hackerworld")    
print hackerrankInString("hhaacckkekraraannk")    
print hackerrankInString("rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt")    