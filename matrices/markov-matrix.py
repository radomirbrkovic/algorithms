# Program for Markov matrix https://www.geeksforgeeks.org/markov-matrix/

def isMarkov(matrix):

    for i in range(len(matrix)):
        if sum(matrix[i]) != 1:
            return False

    return True

m = [ 
      [ 0, 0, 1 ],
      [ 0.5, 0, 0.5 ],
      [ 1, 0, 0 ]     
   ]
 
if (isMarkov(m)) :
    print(" yes ")
else :
    print(" no ")