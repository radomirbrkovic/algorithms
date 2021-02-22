# Library Fine https://www.hackerrank.com/challenges/library-fine/problem

def libraryFine(d1, m1, y1, d2, m2, y2):
    if (d2>=d1 and m2>=m1 and y2>=y1) or (m2>m1 and y2>=y1) or (y2>y1):
        fine=0
    elif d2<d1 and m2==m1 and y2>=y1:
        fine=15*abs(d2-d1)
    elif m2<m1 and y2==y1:
        fine=500*abs(m2-m1)
    else:
        fine=10000

    return fine    

print libraryFine(9, 6, 2015, 6, 6, 2015)              