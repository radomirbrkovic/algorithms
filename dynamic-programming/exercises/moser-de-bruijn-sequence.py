# Moser-de Bruijn Sequence https://www.geeksforgeeks.org/moser-de-bruijn-sequence/

def getMoserDeBruijn(n):
    
    if n <= 1:
        return n

    if n % 2 == 0:
        return 4 * getMoserDeBruijn(n // 2)
    else:
        return 4 * getMoserDeBruijn(n // 2) + 1

def moserDeBruijnSequence(n):
    for i in range(0, n):
        print(getMoserDeBruijn(i), end=" ")   

if __name__=="__main__":
    moserDeBruijnSequence(10)