# Sort elements by frequency https://www.geeksforgeeks.org/sort-elements-by-frequency/

from collections import defaultdict

def sortByFreq(arr):
    d = defaultdict(lambda: 0)

    for i in range(len(arr)):
        d[arr[i]] += 1 


    arr.sort(key = lambda x: (-d[x], x))    
    return (arr)

if __name__ == "__main__":
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    solution = sortByFreq(arr)
    print(*solution)    