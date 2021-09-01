# Find all distinct subsets of a given set using BitMasking Approach https://www.geeksforgeeks.org/find-distinct-subsets-given-set/

def printPowerSet(arr):
    n = len(arr)
    _list = []

    for i in range(2**n):
        subset = ""
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"

        if subset not in _list and len(subset) > 0:
            _list.append(subset)

    for subset in _list:
        arr = subset.split('|')
        for string in arr:
            print(string, end = " ")
        print()        

if __name__ == '__main__':
    arr = [10, 12, 12]
    printPowerSet(arr)