# Lisa's Workbook https://www.hackerrank.com/challenges/lisa-workbook/problem


def workbook(n, k, arr):
    answer = 0
    page = 1

    for probs in arr:
        for i in range(1, probs + 1):
            if i == page:
                answer += 1

            if i == probs or i % k == 0:
                page += 1

    return answer


print workbook(5, 3, [4, 2, 6, 1, 10])