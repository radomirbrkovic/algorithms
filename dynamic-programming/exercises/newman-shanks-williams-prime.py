# Newman–Shanks–Williams prime https://www.geeksforgeeks.org/newman-shanks-williams-prime/

def nswp(n):

    if n <= 1:
        return 1
    return 2 * nswp(n-1) + nswp(n-2)

print(nswp(4)) # 17         