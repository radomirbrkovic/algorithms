# Sorting Big Integers https://www.geeksforgeeks.org/sorting-big-integers/

def sortingBigIntegers(arr):
  arr.sort(key = lambda x: (len(x), x))

arr = ["54", "724523015759812365462", "870112101220845", "8723", "8722"]

sortingBigIntegers(arr)
print (" ".join(arr))