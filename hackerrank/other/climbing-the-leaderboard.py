# Climbing the Leaderboard https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(ranked, player):
    result = []
    sortedList = sorted(list(set(ranked)), reverse=True)
    for score in  sorted(player, reverse=True):
        i = 1
        for rank in sortedList:
            if rank > score:
                i += 1
            else:
                break
        
        result.append(i)             

    return result[::-1]


print climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])