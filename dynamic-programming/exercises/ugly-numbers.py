# Ugly Numbers https://www.geeksforgeeks.org/ugly-numbers/

def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a

def isUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0

# Function to get the nth ugly number
def getNthUglyNo(n):
    i = 1
     
    # ugly number count
    count = 1 
 
    # Check for all integers untill
    # ugly count becomes n
    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i        

print("150th ugly number is ", getNthUglyNo(150))    