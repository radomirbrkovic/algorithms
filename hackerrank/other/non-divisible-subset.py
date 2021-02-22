# Non-Divisible Subset https://www.hackerrank.com/challenges/non-divisible-subset/problem

def nonDivisibleSubset(k, s):
    reminder = [0] * k

    for i in s:
        reminder[i % k] += 1

    maximum = 0
    maximum += min(reminder[0], 1)

    if k % 2 == 0:
       maximum += min(reminder[k // 2], 1) 

    for i in range(1, k // 2 + 1):
        if i != k - i:
            maximum += max(reminder[i], reminder[k - i])       

    return maximum        

print nonDivisibleSubset([1, 7, 2, 4], 3)