# [Find the Running Median]
# (https://www.hackerrank.com/challenges/find-the-running-median/problem)
'''
from heapq import heappop, heappush, heappushpop
            
N = int(input())
S = [int(input()) for i in xrange(N)]
L, R  = [], [S[0]]

for i in xrange(N):
    print "%.1f" % R[0] if len(R)>len(L) else (R[0]-L[0])/2.0
    if i==N-1: break
    heappush(L,-heappushpop(R, S[i+1]))
    if len(L)>len(R): heappush(R,-heappop(L))
'''
from math import floor
            
N = int(input())
S = [int(input()) for i in xrange(N)]
print "\n\n"

j = 1;
for i in S:
    if j == 1:
        result = float(S[0])
    elif j % 2 == 0:
        result = float((float(S[j/2]) + float(S[j/2-1])) / float(2))
    else:
        result = float(S[int(floor(j/2))])

    print result
    j += 1    
   
    
