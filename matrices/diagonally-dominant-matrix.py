# Diagonally Dominant Matrix https://www.geeksforgeeks.org/diagonally-dominant-matrix/

def isDDM(matrix):
    n = len(matrix)
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += abs(matrix[i][j])

        sum -= abs(matrix[i][i])

        if(abs(matrix[i][i]) < sum):
            return False    

    return True        

m = [[ 3, -2, 1 ],
    [ 1, -3, 2 ],
    [ -1, 2, 4 ]]
 
if((isDDM(m))) :
    print ("YES")
else :
    print ("NO")    