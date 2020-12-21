# Cats and a Mouse  https://www.hackerrank.com/challenges/cats-and-a-mouse/problem


def catAndMouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return 'Cat A'
    elif abs(x - z) > abs(y - z):
        return 'Cat B'
    else:
        return 'Mouse C'

print catAndMouse(1, 2, 3)     
print catAndMouse(1, 3, 2)   