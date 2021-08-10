# Power Set in Lexicographic order https://www.geeksforgeeks.org/powet-set-lexicographic-order/

def permuteRec(string, n, index = -1, curr = ""):
    if index == n:
        return
 
    if len(curr) > 0:
        print(curr)
 
    for i in range(index + 1, n):
        curr += string[i]
        permuteRec(string, n, i, curr)
 
        curr = curr[:len(curr) - 1]
 
def powerSet(string):
    string = ''.join(sorted(string))
    permuteRec(string, len(string))
 
if __name__ == "__main__":
    string = "cab"
    powerSet(string)