# Encryption https://www.hackerrank.com/challenges/encryption/problem
import math

def encryption(s):
    s = s.replace(' ', '')
    cols = int(math.ceil(math.sqrt(len(s))))
    matrix = []
    tmpArray = []
    row = 0
    for i in range(len(s)):
        tmpArray.append(s[i])

        if int(math.floor((i+1)/cols)) > row:
            matrix.append(tmpArray)
            row += 1
            tmpArray = []    

    matrix.append(tmpArray)            
    result = []


    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if j < len(matrix) and i < len(matrix[j]):
                result.append(matrix[j][i])
              
        result.append(" ")        

    return "".join(x for x in result)    



print encryption('have a nice day')
print encryption('feed the dog')