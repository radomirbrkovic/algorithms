#Halloween Sale https://www.hackerrank.com/challenges/halloween-sale/problem


def howManyGames(p, d, m, s):

    counter = 0

    while p <= s:
        s -= p
        p = max(p-d, m)
        counter +=1          

    return counter


print howManyGames(20, 3, 6, 85)            