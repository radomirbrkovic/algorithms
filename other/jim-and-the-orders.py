# Jim and the Orders https://www.hackerrank.com/challenges/jim-and-the-orders/problem
import operator

def jimOrders(orders):
    sums = {}

    for i in range(len(orders)):
        sums[i+1] = sum(orders[i])

    return sorted(sums, key=sums.get)  
   




print jimOrders([[1, 3], [2, 3], [3, 3]]) # 1, 2 , 3
print jimOrders([[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]) # 4 2 5 1 3