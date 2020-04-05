# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    totalApples = 0
    totalOranges = 0

    for apple in apples:

        if a + apple >= s and a + apple <= t:
            totalApples +=1

    for orange in oranges:
        if orange + b <= t and orange + b >= s:
            totalOranges += 1

    print totalApples
    print totalOranges        



countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

