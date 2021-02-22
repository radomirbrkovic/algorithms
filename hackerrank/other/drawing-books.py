# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    isEvenPages = n % 2 == 0
    turnedPage = 0

    if p > n / 2 :
        start = n
        while start >= p:
            if isEvenPages:
                if n == start:
                    start -= 1
                else:
                    start -= 2
            else:
                 start -= 2

            if start >= p:     
                turnedPage+=1     


    else:
        start = 1
        while start <= p:
            if start == 1:
                start += 1
            else:
                start += 2
           

            if start <= p:     
                turnedPage+=1     

    return turnedPage    


print pageCount(6,4)
print pageCount(7, 4)

