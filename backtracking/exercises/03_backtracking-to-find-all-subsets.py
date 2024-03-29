# Backtracking to find all subsets https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/

def subsetsUtil(A, subset, index):
    print(*subset)
    for i in range(index, len(A)):
         
        subset.append(A[i])
         
        subsetsUtil(A, subset, i + 1)
         
        subset.pop(-1)
    return

def subsets(A):
    global res
    subset = []
    
    index = 0
    subsetsUtil(A, subset, index)

array = [1, 2, 3]

subsets(array)