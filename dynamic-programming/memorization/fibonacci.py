# Example of calculating Fibonacci nubers by DP Memorization technique
def Fibonacci(n):
    memorize = [-1 for x in range(n+1)]
    return calcFibonacci(memorize, n)

# Helper function for calculating Fibonacci number by recursion
def calcFibonacci(memorize, n):
    
    if n < 2:
        return n

    # if we have already solved this subproblem, simply return the result from the cache
    if memorize[n] >= 0:
        return memorize[n]

    memorize[n] = calcFibonacci(memorize, n-1) + calcFibonacci(memorize, n-1)
    
    return memorize[n]    


if __name__=="__main__":
    print("5th Fibonacci is ---> " + str(Fibonacci(5)))
    print("6th Fibonacci is ---> " + str(Fibonacci(6)))
    print("12th Fibonacci is ---> " + str(Fibonacci(12)))
