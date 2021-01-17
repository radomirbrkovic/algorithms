# Fair Rations https://www.hackerrank.com/challenges/fair-rations/problem


def fairRations(B):
    result = 0
    n = len(B)

    for i in range(n-1):
        if B[i] % 2 != 0:
            result += 2
            B[i+1] += 1 

    if B[n - 1] % 2 != 0:
        return "NO"
    else:
        return result    

    



print fairRations([2, 3, 4, 5, 6])    
print fairRations([1, 2])    