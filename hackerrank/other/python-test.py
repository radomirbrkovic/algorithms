'''
n = "..."
output = ""
for i in range(1, len(n)+1):
    output = output+""+str(i)

print output   
'''
'''
arr = [2, 3, 6, 6, 5]

maxv = max(arr)
l = list(filter(lambda x: x != maxv,arr))
print l

'''

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    total = 0
    for i in range(len(bill)):
        if i != k:
            total += bill[i]

    refound = b - (total/2)        

    if refound > 0:
        print refound
    else:
        print 'Bon Appetit'


bonAppetit([3, 10, 2, 9], 1, 7)

bonAppetit([3, 10, 2, 9], 1, 12)