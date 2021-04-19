# New Year Chaos https://www.hackerrank.com/challenges/new-year-chaos/problem

def minimumBribes(q):

    counter = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                counter += 1

    print(counter)                


minimumBribes([2, 1, 5, 3, 4]) #3
minimumBribes([2, 5, 1, 3, 4]) #Too chaotic 