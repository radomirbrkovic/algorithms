# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem



# Complete the breakingRecords function below.
def breakingRecords(scores):
    minCount = 0
    maxCount = 0
    minScore = 0
    maxScore = 0
    
    for i in range(len(scores)):
        if i == 0:
            minScore = scores[i]
            maxScore = scores[i]
        else:   

            if(scores[i] > maxScore):
                maxScore = scores[i]
                maxCount += 1
            elif(scores[i] < minScore):
                minScore = scores[i]
                minCount += 1

    return [maxCount, minCount]             


input = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
input2 = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print breakingRecords(input2)
