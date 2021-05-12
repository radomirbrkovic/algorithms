# Find median in row wise sorted matrix https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/
from statistics import median

def getMedianOfMatrix(matrix):
    tmp = []

    for row in matrix:
        for i in row:
            tmp.append(i) 

    return median(tmp)     
 

if __name__ == "__main__" :
    m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
    print ("Median is", getMedianOfMatrix(m))