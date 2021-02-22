# Strange Counter https://www.hackerrank.com/challenges/strange-code/problem



def strangeCounter(t):
    time = 3

    while True:
        t -= time

        if t <= 0:
            t += time

            return time - t + 1

        time *= 2



print strangeCounter(4)