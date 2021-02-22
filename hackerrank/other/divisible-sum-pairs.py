# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

input = [1, 3, 2, 6, 1, 2]


def divisibleSumPairs(n, k, ar):
    result = 0

    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1

    return result

print divisibleSumPairs(6, 3, input)