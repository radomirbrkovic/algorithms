# Maximum games played by winner https://www.geeksforgeeks.org/maximum-games-played-winner/

def maxGameByWinner(N):
    dp = [0 for i in range(N)]

    dp[0] = 1
    dp[1] = 2

    i = 1
    while dp[i] <= N:
        i += 1
        dp[i] = dp[i - 1] + dp[i -2] 

    return i - 1    

print(maxGameByWinner(10))    