# Combinational Sum https://www.geeksforgeeks.org/combinational-sum/


def combinationSum(arr, sum):
    ans = []
    temp = []

    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans

def findNumbers(ans, arr, temp, sum, index):
     
    if(sum == 0):
        ans.append(list(temp))
        return
       
    for i in range(index, len(arr)):
        if(sum - arr[i]) >= 0:
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum-arr[i], i)
 
            temp.remove(arr[i])    

arr = [2, 4, 6, 8]
sum = 8
ans = combinationSum(arr, sum)
 

if len(ans) <= 0:
    print("empty")
 
for i in range(len(ans)):
 
    print("(", end=' ')
    for j in range(len(ans[i])):
        print(str(ans[i][j])+" ", end=' ')
    print(")", end=' ')            