# Cut the sticks https://www.hackerrank.com/challenges/cut-the-sticks/problem

result = []
def cutTheSticks(arr):
    minElement = min(arr)
    result.append(len(arr))

    newArray = []

    for i in arr:
        if i > minElement:
            newArray.append(i - minElement)

    if(len(newArray) > 0):
        cutTheSticks(newArray)

    return result    


#print cutTheSticks([5, 4, 4, 2, 2, 8])    
print cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1])    

