# Jumping on the Clouds: Revisited https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy    

print jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2)    
