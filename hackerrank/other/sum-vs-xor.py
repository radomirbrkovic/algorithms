# Sum vs XOR https://www.hackerrank.com/challenges/sum-vs-xor/problem

def sumXor(n):
    count = 0
    while n:
        if n % 2 == 0:
            count += 1
        n = n // 2
    return(2**count)

print sumXor(5) # 2
print sumXor(10) # 4