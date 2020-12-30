# Save the Prisoner! https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(n, m, s):
    ans = (s+m-1)%n

    if ans==0:
        return n

    return ans           

print saveThePrisoner(5, 2, 1)
print saveThePrisoner(5, 2, 2)

print saveThePrisoner(7, 19, 2)
print saveThePrisoner(3, 7, 3)    