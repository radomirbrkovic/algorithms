# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen
def miniMaxSum(arr):
    minArr = list(arr)
    maxArr= list(arr)

    minArr.remove(max(arr))
    maxArr.remove(min(arr))

    print str(sum(minArr))+" "+str(sum(maxArr))


test = [1, 2, 3, 4, 5]

miniMaxSum(test)