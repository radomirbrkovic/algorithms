# Lonely Integer https://www.hackerrank.com/challenges/lonely-integer/problem

def lonelyinteger(a):
    counter = {}
    for i in a:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for i, v in counter.items():
        if v == 1:
            return i

    return None                    

print lonelyinteger([1]) # 1
print lonelyinteger([0, 0, 1, 2, 1]) # 2