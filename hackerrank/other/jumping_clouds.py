#!/bin/python

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    result = 0 

    while i < len(c) - 1:
        if c[i] == 0:
            result += 1

            if i < len(c) - 2 and c[i+2] == 0:
                i+= 2
            else:
                i+=1    
        else:
            i += 1

    return result       

test = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]

print jumpingOnClouds(test)