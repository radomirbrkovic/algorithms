# Strong Password https://www.hackerrank.com/challenges/strong-password/problem
import re

def minimumNumber(n, password):
    count = 0

    #check special caracters
    if not re.search("[!@#$%^&*()-+]", password):
        count += 1

    if not re.search("\d", password):
        count += 1

    if not re.search("[a-z]", password):
        count += 1

    if not re.search("[A-Z]", password):
        count += 1 

    return max(count, 6 -n)


print minimumNumber(3, "Ab1")        
print minimumNumber(11, "#HackerRank")        





    