# https://www.hackerrank.com/challenges/counting-valleys/problem

input = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']



# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    level = 0

    for i in range(n):
        if level == 0 and s[i] == 'D':
            valleys += 1

        if  s[i] == 'D':
            level -= 1

        elif s[i] == 'U':
            level += 1

    return valleys                

print countingValleys(8, input)