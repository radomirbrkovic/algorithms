# Beautiful Triplets  https://www.hackerrank.com/challenges/beautiful-triplets/problem 


def beautifulTriplets(d, arr):
    count = 0
    
    for i in arr:
        if i + d in arr and i + 2*d in arr:
            count += 1 

    return count

print beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10])    