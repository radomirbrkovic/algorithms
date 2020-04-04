# https://www.hackerrank.com/challenges/game-of-stones-1/problem


def gameOfStones(n):
    if ((n - 1) % 7) in [0, 6]:
        return "Second"
    else:
        return "First"


input  = [1, 2, 3, 4, 5, 6, 7, 10]

for i in input:
    print gameOfStones(i)