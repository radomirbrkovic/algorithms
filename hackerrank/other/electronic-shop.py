# https://www.hackerrank.com/challenges/electronics-shop/problem

keyboards = [3, 1] 
drives = [5, 2, 8]

def getMoneySpent(keyboards, drives, b):
    
    result  = -1

    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b and keyboard + drive > result:
                result = keyboard + drive 


    return result

print getMoneySpent(keyboards, drives, 4)    