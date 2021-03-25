# Gaming Array https://www.hackerrank.com/challenges/an-interesting-game-1/problem

def gamingArray(arr):
    moves = 0
    cmax = 0

    for i in range(len(arr)):
        if cmax < arr[i]:
            cmax = arr[i]
            moves += 1
   
    if moves % 2 == 0:
        return 'ANDY'
    else:
        return 'BOB'    

print(gamingArray([5, 2, 6, 3, 4])) #ANDY    
print(gamingArray([3, 1])) #BOB    