# Sub-array Division https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    return  sum([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])


print birthday([1, 2, 1, 3, 2], 3, 2)    
print birthday([1, 1, 1, 1, 1, 1], 3 , 2)

print birthday([4], 4, 1)

print birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7)