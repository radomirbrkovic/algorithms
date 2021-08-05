# Sort an array of large numbers https://www.geeksforgeeks.org/sort-array-large-numbers/

def sortLargeNumbers(arr):
    arr.sort(key = int)


if __name__ == '__main__':
 
    arr = [ "5", "1237637463746732323",
            "97987", "12" ]
 
    sortLargeNumbers(arr)
 
    for i in arr:
        print(i, end = ' ')