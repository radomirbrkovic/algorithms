# Golomb sequence https://www.geeksforgeeks.org/golomb-sequence/

def golomb(n):

    if n == 1:
        return 1

    return 1 + golomb(n - golomb(golomb(n -1)))
   
def getGolomb(n):
    for i in range(1, n +1):
        print(golomb(i), end=" ")


if __name__=="__main__":
    getGolomb(6)     