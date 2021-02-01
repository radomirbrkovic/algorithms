# Permuting Two Arrays https://www.hackerrank.com/challenges/two-arrays/problem

def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    for x,y in zip(A,B):
        if x+y<k:
            return "NO"
    return "YES"  

print twoArrays(10, [2, 1, 3], [7, 8, 9])    
print twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4])    