# https://www.hackerrank.com/challenges/staircase/problem

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        row = ""
        for j in range(1, n+1):
            if n - j > i:
                row += " "
            else:
                row += "#"  
            
        print row

staircase(95)            