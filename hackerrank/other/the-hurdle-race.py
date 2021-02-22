# The Hurdle Race https://www.hackerrank.com/challenges/the-hurdle-race/problem

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maxElement = max(height)

    if k > maxElement:
        return 0
    else:
       return  maxElement - k


print hurdleRace(7, [2, 5, 4, 5, 2])

print hurdleRace(4, [1, 6, 3, 5, 2])
