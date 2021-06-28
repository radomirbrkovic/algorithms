# Minimum removals from array to make max – min <= K https://www.geeksforgeeks.org/minimum-removals-array-make-max-min-k/

def findInd(key, i, n,
            k, arr):
   
     ind = -1
     
     start = i + 1
     end = n - 1;
     
     while (start < end):
          mid = int(start +
                   (end - start) / 2)
         
          if (arr[mid] - key <= k):
               ind = mid
               start = mid + 1
          else:
               end = mid
                 
     return ind
     
def removals(arr, n, k):
   
     ans = n - 1
     
     arr.sort()
     
     for i in range(0, n):
          j = findInd(arr[i], i,
                      n, k, arr)
           
          if (j != -1):
               ans = min(ans, n -
                        (j - i + 1))
 
     return ans
     
a = [1, 3, 4, 9,
     10,11, 12, 17, 20]
n = len(a)
k = 4
print(removals(a, n, k))
