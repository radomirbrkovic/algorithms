# Marc's Cakewalk https://www.hackerrank.com/challenges/marcs-cakewalk/problem

def marcsCakewalk(calorie):
    result = 0
    calorie.sort(reverse=True)
   
    for i in range(len(calorie)):
        result += pow(2, i) * calorie[i]

    return result    

print marcsCakewalk([1, 3, 2])  # 11
print marcsCakewalk([7, 4, 9, 6]) # 79    