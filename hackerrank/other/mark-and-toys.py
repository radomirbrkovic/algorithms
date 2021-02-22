# Mark and Toys https://www.hackerrank.com/challenges/mark-and-toys/problem

def maximumToys(prices, k):
    count = 0
    total = 0

    prices.sort()

    for i in range(len(prices)):
        if total + prices[i] <= k:
            count += 1
            total += prices[i]
        else:
            break    

    return count

print maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)