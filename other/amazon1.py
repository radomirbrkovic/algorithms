'''      
           elif j == len(states) - 1 :   
               output[j] = (1, 0)[states[j - 1] == 0]
           else:
               output[j] = (1, 0)[states[j - 1] == states[j  + 1]]    
'''


def cellCompete(states, days):
   output = list(states)
   for i in range(days):
            
       for j in range(len(states)):
           if j == 0:
               output[0] = 0 if states[1] == 0 else 1
           elif j == len(states) - 1 :   
               output[j] = 0 if states[j - 1] == 0 else 1
           else:
               output[j] = 0 if states[j - 1] == states[j + 1] else 1   

            
       states = list(output)
    
   return states         
    


test1 = [1, 0,0,0, 1,0,0]

print cellCompete(test1, 1)