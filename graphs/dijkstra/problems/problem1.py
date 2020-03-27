input = [9, 4] 
#code
for n in input:
    count = 0
    while n != 1:
        if n%3 == 0:
            n //= 3
        else:
            n -= 1
        count += 1
    print(count)
