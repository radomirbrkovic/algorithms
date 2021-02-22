# The Grid Search https://www.hackerrank.com/challenges/the-grid-search/problem

def gridSearch(G, P):

    def check(x, y):
        for i in range(r):
            if P[i] != G[x+i][y:y+c]:
                return False
        return True

    for i in range(R):
        for j in range(C):
            if G[i][j] == P[0][0]:
                if check(i, j):
                    return 'YES'

    return "NO"                


