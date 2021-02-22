# Sherlock and The Beast https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

def decentNumber(n):
    three = n//3
    
    while (n - 3*three)%5 != 0:
        #print("three = {} five = {}".format(three, (n - 3*three)//5))
        three -= 1
        
    if three > 0:
        res = [5] * 3 * three
        res += [3] * (n - 3*three)
    elif three == 0 and n%5 == 0:
        res = [3] * n
    else:
        res = [-1]
    
    print "".join(map(str, res))    

decentNumber(1)
decentNumber(3)
decentNumber(5)
decentNumber(11)
decentNumber(7)
decentNumber(4)
decentNumber(15)
