# https://www.hackerrank.com/challenges/grading/problem

def fiveRound(x):
    if x % 5 == 0:
        return x
    else: 
        for i in range(1, 5):
            if (i + x) % 5 == 0:
              return  i + x 

    return x          

def gradingStudents(grades):
    output = []
    for i in grades:
        if i >= 38:
            j = fiveRound(i)
            if abs(j - i) < 3:
                output.append(j)
            else:
                output.append(i)     
        else:
            output.append(i)

    return output



input = [73, 67, 38, 33]
input2 = [80, 96, 18, 73, 78, 60, 60, 15, 45, 15, 10, 5, 46, 87, 33, 60, 14, 71, 65, 2, 5, 97, 0]

print gradingStudents(input2)