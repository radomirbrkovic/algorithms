# Fibonacci Modified https://www.hackerrank.com/challenges/fibonacci-modified/problem

def fibonacciModified(t1, t2, n):
    sequence = [t1, t2]
    if n <= 2:
        return sequence[n-1]
    else:
        for i in range(n-2):
            sequence.append(sequence[-2] + sequence[-1]**2)
    
    return sequence[-1]


print(fibonacciModified(0, 1, 5)) #5   