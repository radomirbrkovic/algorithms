# https://www.hackerrank.com/challenges/camelcase/problem

# Complete the camelcase function below.
def camelcase(s):
    result = 1

    for i in s:
        if i.isupper() :
            result += 1


    return result

input  = "saveChangesInTheEditor"

print camelcase(input)