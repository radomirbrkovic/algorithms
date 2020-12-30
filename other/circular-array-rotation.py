# Circular Array Rotation https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
   n=len(a)
   result = []

   for q in queries:
       result.append(a[(n-k+q)%n])
   
   return result    

print circularArrayRotation([1, 2, 3], 2, [0,1,2])        
