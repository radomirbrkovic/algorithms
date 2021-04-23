# Program for nth Catalan Number https://www.geeksforgeeks.org/program-nth-catalan-number/

def nthCatalan(n):
    
    if n <= 1:
        return 1

    result = 0

    for i in range(n):
        result += nthCatalan(i) * nthCatalan(n - 1 - i) 
    
    return result        

for i in range(15):
    print(nthCatalan(i))    