# Goodland Electricity https://www.hackerrank.com/challenges/pylons/problem

def pylons(k, arr):
    i = 0
    c = 0 
    n = len(arr)
    while True:
        u =  min(i+2*k-1,n) if i else min(i+k,n)
        for i in range(i,u)[::-1]:
            if arr[i]:
                c+=1
                if i+k>=n: 
                    return c
                i+=1
                break
        else:
            return -1    

    


print(pylons(2, [0, 1, 1, 1, 1, 0])) #2