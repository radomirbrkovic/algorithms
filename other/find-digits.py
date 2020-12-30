# Find Digits https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):
    
    output = 0
    for digit in str(n):
        if int(digit) > 0 and n % int(digit) == 0:
            output += 1

    return output


print findDigits(12)
print findDigits(1012)