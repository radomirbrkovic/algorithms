# Priyanka and Toys https://www.hackerrank.com/challenges/priyanka-and-toys/problem

def toys(w):
    result = 1
    w.sort()
    target = w[0]

    for i in range(1, len(w)):
        if w[i] > target + 4:
            target = w[i]
            result += 1

    return result





print toys([12, 15, 7, 8, 19, 24]) # 4 
print toys([1, 2, 3, 21, 7, 12, 14, 21]) # 4
