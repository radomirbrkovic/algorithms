#Birthday Cake Candles https://www.hackerrank.com/challenges/birthday-cake-candles/problem
 

def birthdayCakeCandles(candles):
    max = 0
    countMax = 0

    for candle in candles:
        if candle > max:
            max = candle
            countMax = 1
        elif  candle == max:
            countMax = countMax + 1

    return countMax

print birthdayCakeCandles([3, 2, 1, 3])               