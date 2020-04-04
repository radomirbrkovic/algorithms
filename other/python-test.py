'''
n = "..."
output = ""
for i in range(1, len(n)+1):
    output = output+""+str(i)

print output   
'''

arr = [2, 3, 6, 6, 5]

maxv = max(arr)
l = list(filter(lambda x: x != maxv,arr))
print l
