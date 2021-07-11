# Two elements whose sum is closest to zero https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/

def minAbsSumPair(arr):
    invCount = 0
    n = len(arr)

    if n < 2:
        print("Invalid Input")
        return

    minI = 0
    minJ = 0 

    minSum = arr[0] + arr[1]

    for i in range(n - 1 ):
        for j in range(i + 1, n):
            sumTmp = arr[i] + arr[j]

            if abs(minSum) > abs(sumTmp):
                   minSum = sumTmp
                   minI = i
                   minJ = j

    print(f"The two elements whose sum is minimum are {arr[minI]} and  {arr[minJ]} and sum is {minSum}")

minAbsSumPair([1, 60, -10, 70, -80, 85])                    