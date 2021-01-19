# Big Sorting https://www.hackerrank.com/challenges/big-sorting/problem

def bigSorting(unsorted):
    unsorted.sort(key = lambda x: (len(x), x))

    return unsorted


print bigSorting(['1', '2', '100', '12303479849857341718340192371', '3084193741082937', '3084193741082938', '111', '200'])