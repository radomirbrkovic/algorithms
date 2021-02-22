# Mars Exploration https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    result = 0
    oPosition = 1
    for i in range(0, len(s)):
        if i > 0 and (i + 1) % 3 == 0 :
            oPosition += 3

        if i == oPosition:
            if s[i] != "O":
                result += 1
        else:
            if s[i] != "S":
                result += 1        

    return result

print marsExploration("SOSSPSSQSSOR")
print marsExploration("SOSSOT")
print marsExploration("SOSSOSSOS")

