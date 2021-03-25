# Greedy Florist https://www.hackerrank.com/challenges/greedy-florist/problem

def getMinimumCost(k, c):
    result = 0
    cnt = 0

    c = sorted(c, key=lambda x: -x)

    for el in c:
        result += el * (1 + cnt // k)
        cnt += 1

    return result    


print(getMinimumCost(3, [2, 5, 6])) # 13
print(getMinimumCost(3, [1, 3, 5, 7, 9])) # 29