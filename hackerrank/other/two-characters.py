# Two Characters https://www.hackerrank.com/challenges/two-characters/problem

def alternate(s):
    maxNum = count = 0
    alp = list(set(s))

    for i in range(len(alp)):
        for j in range(i+1, len(alp)):
            l = [alp[i], alp[j]]

            if s.index(alp[i]) < s.index(alp[j]):
                ind = 0
            else:
                ind = 1

            for char in s:
                if char in l:
                    if char == l[ind]:
                        count += 1
                        ind = ind ^ 1
                    else:
                        count = 0
                        break
            maxNum  = max(maxNum, count)    
            count = 0   
    return maxNum                     

print(alternate('beabeefeab')) #5