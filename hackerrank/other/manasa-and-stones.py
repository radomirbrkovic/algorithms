# Manasa and Stones https://www.hackerrank.com/challenges/manasa-and-stones/problem


def stones(n, a, b):
    result = set()

    if a > b:
        a, b = b,a

    for i in range(n):
        result.add(i * a + (n-1 - i) * b)

    return sorted(list(result))    








print stones(3, 1, 2)
print stones(4, 10, 100)