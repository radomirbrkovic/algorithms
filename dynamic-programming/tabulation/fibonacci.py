# Example of calculating Fibonacci nubers by DP Tabulation technique

def Fibonacci(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
    
  return dp[n]


if __name__=="__main__":
    print("5th Fibonacci is ---> " + str(Fibonacci(5)))
    print("6th Fibonacci is ---> " + str(Fibonacci(6)))
    print("12th Fibonacci is ---> " + str(Fibonacci(12)))