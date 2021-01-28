# Making Anagrams https://www.hackerrank.com/challenges/making-anagrams/problem
from collections import Counter
def makingAnagrams(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)

    total = (d1 - d2) + (d2 - d1)
    return sum(total.values())

print makingAnagrams('cde', 'abc')