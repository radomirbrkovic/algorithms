# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def plusMinus(arr):
    positive = 0;
    negative = 0;
    zero = 0;

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    print float(positive) / float(len(arr))
    print float(negative) / float(len(arr))
    print float(zero) / float(len(arr))

arr = [-4, 3, -9, 0, 4, 1]


 plusMinus(arr)