# Maximizing XOR https://www.hackerrank.com/challenges/maximizing-xor/problem

def maximizingXor(l, r):
    
    max = 0
    while l <= r:
        for i in range(l, r+1):
            if l ^ i > max:
                max = l ^ i

        l += 1           

    return max


print maximizingXor(10, 15)  # 7  
print maximizingXor(11, 100) # 127   