# Utopian Tree https://www.hackerrank.com/challenges/utopian-tree/problem

# Complete the utopianTree function below.
def utopianTree(n):
   return pow(2,(n+2)//2)-1 if n%2==0 else pow(2,(n+3)//2) - 2


for i in [54, 52, 47, 48, 49, 53, 46, 50, 51, 55]:
    print utopianTree(i)

