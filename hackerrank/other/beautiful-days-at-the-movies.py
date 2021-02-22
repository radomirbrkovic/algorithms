# Beautiful Days at the Movies https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i, j, k):
    result = []
    for day in range(i, j +1):
        different = abs(day - getReverseNumber(day)) / float(k)
        if (different).is_integer(): 
            result.append(day)

    return len(result)        

def getReverseNumber(number):
    revs_number = 0  
    while (number > 0):  
        # Logic  
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10  

    return revs_number

print beautifulDays(20, 23, 6)
