# Convert an array to reduced form  https://www.geeksforgeeks.org/convert-an-array-to-reduced-form-set-1-simple-and-hashing/


def convert(arr, n):
    tmp = arr.copy()

    tmp.sort()
    m = {}
    val = 0

    for i in range(n):
        m[tmp[i]] = val
        val += 1

    for i in range(n):
        arr[i] = m[arr[i]]

def printArr(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
 
# Driver Code
if __name__ == "__main__":
    arr = [10, 20, 15, 12, 11, 50]
    n = len(arr)
    print("Given Array is ")
    printArr(arr, n)
    convert(arr , n)
    print("\n\nConverted Array is ")
    printArr(arr, n)             